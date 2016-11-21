# This object will be in charge of interacting with the API, and storing the objects into the database.
from CategoriesAPI import CategoriesAPI
from PlaylistAPI import PlaylistAPI
from TrackAPI import TrackAPI
from AudioFeatureAPI import AudioFeatureAPI
import Security
import MySQLdb

def generateInsertQuery(tablename, columns, values):
	sqlClause = "INSERT INTO "+tablename+" "+columns+" VALUES "
	params = "("+",".join(["%s" for x in values])+")"
	sqlClause += params
	return sqlClause, values

def loadCategories():
	def getQueries(listOfCategories):
		statements = []
		for c in listOfCategories:
			col,values = c.toSQLInsert()
			sqlQuery, val = generateInsertQuery('Category',col,values)
			statements.append((sqlQuery,val))
		return statements

	cAPI = CategoriesAPI()
	cAPI.getCategories()
	listOfCategories = cAPI.list_of_categories
	print(len(listOfCategories))
	return getQueries(listOfCategories)

def loadPlaylist(categoryID):
	def savePlaylist(listOfPlaylist, categoryID):
		statements = []
		param = {"categoryID":categoryID}
		for p in listOfPlaylist:
			col,values = p.toSQLInsert(param)
			sqlQuery, values = generateInsertQuery('Playlist',col,values)
			statements.append((sqlQuery, values))
		return statements
			

	pAPI = PlaylistAPI(categoryID)
	pAPI.getPlaylists()
	listOfPlaylist = pAPI.list_of_playlist
	return savePlaylist(listOfPlaylist,categoryID)

def loadTracks(userID, playlistID):
	def saveTracks(listOfTracks, playlistID):
		param = {"playlistID":playlistID}
		statements = []
		for p in listOfTracks:
			col,values = p.toSQLInsert(param)
			sqlQuery, val = generateInsertQuery('Track',col,values)
			statements.append((sqlQuery, values))
		return statements

	tAPI = TrackAPI(userID, playlistID)
	tAPI.getTracks()
	listOfTracks = tAPI.list_of_tracks
	return saveTracks(listOfTracks,playlistID)

def loadAudioFeatures(tracksIds):
	def saveAudioFeatures(dictOfAudioFeatures):
		statements = []
		for afkey in dictOfAudioFeatures:
			param = {"trackID":afkey}
			col,values = dictOfAudioFeatures[afkey].toSQLInsert(param)
			sqlQuery, val = generateInsertQuery('AudioFeatures',col,values)
			statements.append((sqlQuery, values))
		return statements

	afAPI = AudioFeatureAPI(tracksIds)
	afAPI.getAudioFeatures()
	dictOfAudioFeatures = afAPI.dict_audio_features
	return saveAudioFeatures(dictOfAudioFeatures)


def getDBConnection():
	db = MySQLdb.connect(host="localhost",    # your host, usually localhost
	                     user="root",         # your username
	                     passwd="root",  # your password
	                     db="test_py",
	                     charset='utf8')        # name of the data base
	return db

def storeCategories():

	#TODO: Query the cat table if it is empty, load it, else nothing
	sql_queries = loadCategories()
	conn = getDBConnection()
	cursor = conn.cursor()
	print("Adding ",len(sql_queries), " categories")
	for query in sql_queries:
		insert_st = query[0]
		values_st = query[1]
		cursor.execute(insert_st,values_st)		
	conn.commit()
	conn.close()

# 

# TODO: I am hardcoding the list of Categories that we are actually gonna load. This should be better modeled into the db or sth.
categories_used = ["pop","blues","country","hiphop","metal","jazz","punk","reggae","rnb","rock","classical"] #"romance" "soul"

def storePlaylists(categ = []):
	conn = getDBConnection()
	cursor = conn.cursor()
	for cat in categ:
		sql_queries = loadPlaylist(cat)
		print("Adding ",len(sql_queries)," playlists to ",cat)
		for query in sql_queries:
			insert_st = query[0]
			values_st = query[1]
			try:
				cursor.execute(insert_st,values_st)
			except (MySQLdb.Error) as e:
				print(e)
				# print("Trying to executy this query ", insert_st, " -> ",values_st)
			
			conn.commit()
	
	conn.close()

def storeTracks():
	conn = getDBConnection()
	cursor = conn.cursor()
	cursor.execute("SELECT c.ID from Category c")
	catResults = cursor.fetchall()

	for cate in catResults:
		catID = cate[0]
		cursor.execute("SELECT p.ID, p.ownerId from Playlist p INNER JOIN Category c ON p.categoryID = c.ID WHERE c.ID = %s",(catID,))
		results = cursor.fetchall()
		countOfSongs = 0
		print("Processing Category: ",catID)
		for result in results:
			playlistID = result[0]
			ownerID = result[1]
			sqlqueries = loadTracks(ownerID,playlistID)		
			
			if countOfSongs < 100:
				print("Adding ",len(sqlqueries)," tracks")
				for query in sqlqueries:
					insert_st = query[0]
					values_st = query[1]
					try:
						cursor.execute(insert_st,values_st)
						countOfSongs += 1
					except (MySQLdb.Error) as e:
						print(e)

					conn.commit()

	conn.close()

store_audio_page_size = 99
def storeAudioFeatures():
	conn = getDBConnection()
	cursor = conn.cursor()
	cursor.execute("SELECT t.ID from Track t")
	tracks = cursor.fetchall()
	numberOfTracks = len(tracks)
	tracksProcessed = 0
	print("Going to process ",numberOfTracks,"number of tracks")
	while (tracksProcessed < numberOfTracks):
		toProcess = numberOfTracks - tracksProcessed
		amount = store_audio_page_size
		if (toProcess < store_audio_page_size):
			amount = toProcess
		trackList = []
		freezeTracksProcessed = tracksProcessed
		print("Processing songs from:",freezeTracksProcessed," to  ",freezeTracksProcessed + amount)
		for index in range(freezeTracksProcessed, tracksProcessed + amount):
			# print("Index ",index," tracksProcessed: ", tracksProcessed, " amount ", amount, " tracks: ",len(tracks), "freese ",freezeTracksProcessed," tope ",freezeTracksProcessed+index)
			track = tracks[index]
			trackList.append(track[0])
			tracksProcessed += 1
		sqlqueries = loadAudioFeatures(trackList)
		for query in sqlqueries:
			insert_st = query[0]
			values_st = query[1]
			try:
				cursor.execute(insert_st,values_st)
			except (MySQLdb.Error) as e:
				print(e)

			conn.commit()


# Security.renew_access_token()

storeCategories()
storePlaylists(categories_used)
storeTracks()
storeAudioFeatures()


	
