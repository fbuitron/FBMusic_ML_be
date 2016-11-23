from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL
from MachineLearning import Classification
from MachineLearning import Clustering
from MachineLearning import Preprocessing
from flask import request
from flask import jsonify
from SearchAPI import SearchAPI
from AudioFeatureAPI import AudioFeatureAPI
import numpy as np
import json

# Thid onbject is in charge of the REST API with FLASK integration.
# There are all the interfaces for the different services and the controller that reponds to it.

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'test_py'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/classify/knn", methods=['GET'])
def knn():
	k = request.args.get('k')
	accuracy = Classification.classify_KNN(int(k))
	return accuracy

@app.route("/classify/tree", methods=['GET'])
def tree():
	accuracy = Classification.classify_Tree()
	return accuracy

@app.route("/classify/song", methods=['GET'])
def classifySong():
	songId = request.args.get('songId')
	audFeat = AudioFeatureAPI([songId])
	audFeat.getAudioFeatures()
	dictAudFeature = audFeat.dict_audio_features
	
	af = dictAudFeature[songId]
	af_arr = np.array([af.acousticness,af.danceability, af.duration_ms, af.energy, af.instrumentalness, af.key, af.liveness, af.loudness, af.mode, af.speechiness, af.tempo, af.time_signature, af.valence])
	cate = Classification.classify_song_tree(af_arr)
	return cate

@app.route("/cluster/knnMeans", methods=['GET'])
def knnMeans():
	k = request.args.get('k')
	jsonResponse = Clustering.cluster_Kmeans(int(k))
	return jsonify(**jsonResponse)

@app.route("/search/track", methods=['GET'])
def searchTrack():
	q = request.args.get('q')
	est = SearchAPI()
	est.getSearch(q)
	listOfSongs = est.result_list
	return jsonify(listOfSongs)

@app.route("/data/describe", methods=['GET'])
def dataDescribe():
	listResponse = Preprocessing.getDataFeatures()
	return jsonify(**listResponse)	

if __name__ == "__main__":
    app.run()

