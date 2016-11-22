import numpy as np
import pandas as pd
from sklearn import neighbors
import MySQLdb
import csv

#Raw data Query to know how many songs per Category I have
#select c.name, count(t.id) from Track t INNER JOIN Playlist p ON p.ID = t.playlistID INNER JOIN Category c ON c.ID = p.categoryID GROUP BY c.name;
# SELECT cats.id from (SELECT c.id , count(t.id) from Track t INNER JOIN Playlist p ON p.ID = t.playlistID INNER JOIN Category c ON c.ID = p.categoryID  GROUP BY c.id) as cats;
# query = "SELECT c.id, count(t.id) from Track t INNER JOIN Playlist p ON p.ID = t.playlistID INNER JOIN Category c ON c.ID = p.categoryID GROUP BY c.id LIMIT 1;"
#Query to get 100 from each category. This AVOIDS all the NULLS
# SELECT af.trackID, af.acousticness,af.danceability, af.duration_ms, af.energy, af.instrumentalness, af.a_key, af.liveness, af.loudness, af.a_mode, af.speechiness, af.tempo, af.time_signature, af.valence, c.id  FROM AudioFeatures af INNER JOIN Track t ON t.ID = af.trackID INNER JOIN Playlist p ON p.id = t.playlistID INNER JOIN Category c ON p.categoryID = c.ID WHERE c.ID = 'classical' AND af.acousticness IS NOT NULL AND af.danceability IS NOT NULL AND af.duration_ms IS NOT NULL AND af.energy IS NOT NULL AND af.instrumentalness IS NOT NULL AND af.a_key IS NOT NULL AND af.liveness IS NOT NULL AND af.loudness IS NOT NULL AND af.a_mode IS NOT NULL AND  af.speechiness IS NOT NULL AND af.tempo IS NOT NULL AND af.time_signature IS NOT NULL AND af.valence LIMIT 100;

def getDBConnection():
	db = MySQLdb.connect(host="localhost",    # your host, usually localhost
	                     user="root",         # your username
	                     passwd="root",  # your password
	                     db="test_py",
	                     charset='utf8')        # name of the data base
	return db

def getRawData():
	dbConn = getDBConnection()
	cursor = dbConn.cursor()
	
	query = "SELECT af.trackID, af.acousticness,af.danceability, af.duration_ms, af.energy, af.instrumentalness, af.a_key, af.liveness, af.loudness, af.a_mode, af.speechiness, af.tempo, af.time_signature, af.valence, c.id  FROM AudioFeatures af INNER JOIN Track t ON t.ID = af.trackID INNER JOIN Playlist p ON p.id = t.playlistID INNER JOIN Category c ON p.categoryID = c.ID WHERE af.acousticness IS NOT NULL AND af.danceability IS NOT NULL AND af.duration_ms IS NOT NULL AND af.energy IS NOT NULL AND af.instrumentalness IS NOT NULL AND af.a_key IS NOT NULL AND af.liveness IS NOT NULL AND af.loudness IS NOT NULL AND af.a_mode IS NOT NULL AND  af.speechiness IS NOT NULL AND af.tempo IS NOT NULL AND af.time_signature IS NOT NULL AND af.valence AND c.ID in (SELECT cats.id from (SELECT c.id , count(t.id) from Track t INNER JOIN Playlist p ON p.ID = t.playlistID INNER JOIN Category c ON c.ID = p.categoryID  GROUP BY c.id) as cats) LIMIT 20"
	cursor.execute(query)
	results = cursor.fetchall()
	return results

def writeCSV(listResults, filePath, titles=[]):	
	with open(filePath, 'w') as myFile:
		file_writer = csv.writer(myFile)
		file_writer.writerow([x for x in titles])
		for i in range(len(listResults)):
			print(listResults[i])
			file_writer.writerow([x for x in listResults[i]])

titles = ['trackID', 'acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness', 'a_key', 'liveness', 'loudness', 'a_mode', 'speechiness', 'tempo', 'time_signature', 'valence', 'category']
# listResults = getRawData()
# writeCSV(listResults, 'songs.csv', titles)
# def testPandas():
# 	df = pd.read_csv("songs.csv")
# 	print(df.describe())

# testPandas()



