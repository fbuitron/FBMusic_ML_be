# This object will be in charge of interacting with the API, and storing the objects into the database.
from CategoriesAPI import CategoriesAPI
from PlaylistAPI import PlaylistAPI
from TrackAPI import TrackAPI
from AudioFeatureAPI import AudioFeatureAPI
import Security
import MySQLdb


# def testSQL():
# 	db = MySQLdb.connect(host="localhost",    # your host, usually localhost
# 	                     user="root",         # your username
# 	                     passwd="root",  # your password
# 	                     db="test_py")        # name of the data base

# 	# # you must create a Cursor object. It will let
# 	# #  you execute all the queries you need
# 	cur = db.cursor()

# 	# INSERT INTO Track (ID,href,name,playbackURL,popularity,albumName,albumImageURL,artistID,artistName,playlistID) VALUES (?,?,?,?,?,?,?,?,?) ('1mLBSbBqgwg1EIO7h52sdZ', 'https://api.spotify.com/v1/tracks/1mLBSbBqgwg1EIO7h52sdZ', "I'd Rather Go Blind", 'https://p.scdn.co/mp3-preview/bf8550dffd3b09a734580e1ec8b615796ed124eb', '23', '2am Rough Tracks', 'https://i.scdn.co/image/7ce5720197da73267736232a8f52ae191e08adc9', '022EiWsch2zvty0qBUksDO', 'Liam Bailey')
# 	# # Use all the SQL you like
# 	# INSERT INTO Track (ID,href,name,playbackURL,popularity,albumName,albumImageURL,artistID,artistName,playlistID) VALUES (?,?,?,?,?,?,?,?,?,?) ('1mLBSbBqgwg1EIO7h52sdZ', 'https://api.spotify.com/v1/tracks/1mLBSbBqgwg1EIO7h52sdZ', "I'd Rather Go Blind", 'https://p.scdn.co/mp3-preview/bf8550dffd3b09a734580e1ec8b615796ed124eb', '23', '2am Rough Tracks', 'https://i.scdn.co/image/7ce5720197da73267736232a8f52ae191e08adc9', '022EiWsch2zvty0qBUksDO', 'Liam Bailey', '2XYm3JdmAKSWRsj75YRLBV')

# 	# INSERT INTO AudioFeatures (acousticness,danceability,duration_ms,energy,instrumentalness,key,liveness,loudness,mode,speechiness,tempo,time_signature,valence,trackID) VALUES (0.205, 0.51, 221280, 0.688, 0, 7, 0.16, -5.952, 1, 0.0322, 129.795, 4, 0.438, '3LcrBMmEejUO09Lrmyixzb')

# 	# INSERT INTO Category (ID,href,name,imageURL) VALUES (%s,%s,%s,%s) 
# 	# INSERT INTO Category (ID,href,name,imageURL) VALUES (%s,%s,%s,%s) ", ('travel', 'https://api.spotify.com/v1/browse/categories/travel', 'Travel', 'https://t.scdn.co/media/derived/travel-274x274_1e89cd5b42cf8bd2ff8fc4fb26f2e955_0_0_274_274.jpg')
# 	#INSERT INTO Playlist (ID,href,name,imageURL,ownerID,categoryID) VALUES (%s,%s,%s,%s,%s,%s) ('6a3N3HKBQdxIScNB3MsOtg', 'https://api.spotify.com/v1/users/spotify/playlists/6a3N3HKBQdxIScNB3MsOtg', 'Commute Pump Up', 'https://u.scdn.co/images/pl/default/38eb1fa0004cd7116a2ab10f9e5037876b89bae3', 'spotify', 'travel')
# 	# cur.execute("INSERT INTO Category (ID,href,name,imageURL) VALUES (%s,%s,%s,%s) ", ('travel', 'https://api.spotify.com/v1/browse/categories/travel', 'Travel', 'https://t.scdn.co/media/derived/travel-274x274_1e89cd5b42cf8bd2ff8fc4fb26f2e955_0_0_274_274.jpg'))
# 	#cur.execute("INSERT INTO Playlist (ID,href,name,imageURL,ownerID,categoryID) VALUES (%s,%s,%s,%s,%s,%s)",('6a3N3HKBQdxIScNB3MsOtg', 'https://api.spotify.com/v1/users/spotify/playlists/6a3N3HKBQdxIScNB3MsOtg', 'Commute Pump Up', 'https://u.scdn.co/images/pl/default/38eb1fa0004cd7116a2ab10f9e5037876b89bae3', 'spotify', 'travel'))
	
# 	# INSERT INTO Track (ID,href,name,playbackURL,popularity,albumName,albumImageURL,artistID,artistName,playlistID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ('7267sjVo1XgIcKrHsoCjkC', 'https://api.spotify.com/v1/tracks/7267sjVo1XgIcKrHsoCjkC', 'Fort Knox [2012 Edit]', 'None', '0', 'Goldfish', 'https://i.scdn.co/image/0b16593d4043f3ba84f76a962e3e110e366ac3b6', '0uRdK8gy7fXJGRywrlmPM7', 'GoldFish', '6a3N3HKBQdxIScNB3MsOtg')
# 	# cur.execute("INSERT INTO Track (ID,href,name,playbackURL,popularity,albumName,albumImageURL,artistID,artistName,playlistID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",('7267sjVo1XgIcKrHsoCjkC', 'https://api.spotify.com/v1/tracks/7267sjVo1XgIcKrHsoCjkC', 'Fort Knox [2012 Edit]', 'None', '0', 'Goldfish', 'https://i.scdn.co/image/0b16593d4043f3ba84f76a962e3e110e366ac3b6', '0uRdK8gy7fXJGRywrlmPM7', 'GoldFish', '6a3N3HKBQdxIScNB3MsOtg'))
# 	# cur.execute("INSERT INTO Track (ID,href,name,playbackURL,popularity,albumName,albumImageURL,artistID,artistName,playlistID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",('7267sjVo1XgIcKrHsoCjkC', 'https://api.spotify.com/v1/tracks/7267sjVo1XgIcKrHsoCjkC', 'Fort Knox [2012 Edit]', 'None', '0', 'Goldfish', 'https://i.scdn.co/image/0b16593d4043f3ba84f76a962e3e110e366ac3b6', '0uRdK8gy7fXJGRywrlmPM7', 'GoldFish', '6a3N3HKBQdxIScNB3MsOtg'))
# 	# # print all the first cell of all the rows
# 	# for row in cur.fetchall():
# 	#     print(row[0])

# 	# INSERT INTO AudioFeatures (acousticness,danceability,duration_ms,energy,instrumentalness,a_key,liveness,loudness,a_mode,speechiness,tempo,time_signature,valence,trackID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) (0.0571, 0.694, 189767, 0.676, 0, 1, 0.306, -7.627, 1, 0.187, 121.136, 4, 0.621, '7267sjVo1XgIcKrHsoCjkC')
# 	# cur.execute("SELECT * FROM tbl_user WHERE user_id > 2")
# 	cur.execute("INSERT INTO AudioFeatures (acousticness,danceability,duration_ms,energy,instrumentalness,a_key,liveness,loudness,a_mode,speechiness,tempo,time_signature,valence,trackID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(0.0571, 0.694, 189767, 0.676, 0, 1, 0.306, -7.627, 1, 0.187, 121.136, 4, 0.621, '7267sjVo1XgIcKrHsoCjkC'))
# 	# print("Second one!!!")
# 	# # print all the first cell of all the rows
# 	# for row in cur.fetchall():
# 	#     print(row[0])
# 	db.commit()
# 	db.close()

def generateInsertQuery(tablename, columns, values):
	sqlClause = "INSERT INTO "+tablename+" "+columns+" VALUES "
	params = "("+",".join(["%s" for x in values])+")"
	sqlClause += params
	return sqlClause, values


def loadCategories():
	def saveCategories(listOfCategories):
		for c in listOfCategories:
			col,values = c.toSQLInsert()
			sqlQuery, val = generateInsertQuery('Category',col,values)
			print(sqlQuery,val)

	cAPI = CategoriesAPI()
	cAPI.getCategories()
	listOfCategories = cAPI.list_of_categories
	print(len(listOfCategories))
	saveCategories(listOfCategories)

def loadPlaylist(categoryID):
	def savePlaylist(listOfPlaylist, categoryID):
		param = {"categoryID":categoryID}
		for p in listOfPlaylist:
			col,values = p.toSQLInsert(param)
			sqlQuery, values = generateInsertQuery('Playlist',col,values)
			print(sqlQuery, values)
			

	pAPI = PlaylistAPI(categoryID)
	pAPI.getPlaylists()
	listOfPlaylist = pAPI.list_of_playlist
	print(len(listOfPlaylist))
	savePlaylist(listOfPlaylist,categoryID)

def loadTracks(userID, playlistID):
	def saveTracks(listOfTracks, playlistID):
		param = {"playlistID":playlistID}
		for p in listOfTracks:
			col,values = p.toSQLInsert(param)
			sqlQuery, val = generateInsertQuery('Track',col,values)
			print(sqlQuery, values)

	tAPI = TrackAPI(userID, playlistID)
	tAPI.getTracks()
	listOfTracks = tAPI.list_of_tracks
	print(len(listOfTracks))
	saveTracks(listOfTracks,playlistID)

def loadAudioFeatures(tracksIds):
	def saveAudioFeatures(dictOfAudioFeatures):
		for afkey in dictOfAudioFeatures:
			param = {"trackID":afkey}
			col,values = dictOfAudioFeatures[afkey].toSQLInsert(param)
			sqlQuery, val = generateInsertQuery('AudioFeatures',col,values)
			print(sqlQuery, values)

	afAPI = AudioFeatureAPI(tracksIds)
	afAPI.getAudioFeatures()
	dictOfAudioFeatures = afAPI.dict_audio_features
	print(len(dictOfAudioFeatures))
	saveAudioFeatures(dictOfAudioFeatures)
