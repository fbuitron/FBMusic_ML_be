from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import Preprocessing as pre
from sklearn.metrics import completeness_score, homogeneity_score
from sklearn.decomposition import PCA

def cluster():
	dataSet = pre.getDataFromCSV()
	data_ = dataSet.iloc[:,1:-1]
	labels_ = dataSet.iloc[:,-1]
	ids_ = dataSet.iloc[:,0]
	norm_data = pre.completePreprocessing(data_,data_)
	kmeans = KMeans(n_clusters=11).fit(norm_data)
	print(kmeans.labels_[:250])
	print("sklearn clustering scores!!!")
	scoreClusters(kmeans.labels_, labels_)

def myCluster(data_, labels_):
	# dataSet = pre.getDataFromCSV()
	# data_ = dataSet.iloc[:,1:-1]
	# labels_ = dataSet.iloc[:,-1]
	# ids_ = dataSet.iloc[:,0]
	# norm_data = pre.completePreprocessing(data_,data_)
	cen, clussAss = kMeans(data_,11, dist_i_cosine_similarity)
	print(clussAss[:250])
	for cluster in range(11):
		print(getClusterSize(cluster,clussAss))
	predicted_clusters = np.array([int(v) for v in clussAss[:,0]])
	print(predicted_clusters)
	print("my Scores!!!!!")
	scoreClusters(predicted_clusters, labels_)


categories = ['blues','classical','country','hiphop','jazz','metal','pop','punk','reggae','rnb','rock']  

def transform_labels_to_numbers(labels_):
	i=0
	categ = np.zeros(shape=labels_.shape)
	for cat in categories:
		catTrues = labels_ == cat
		categ[np.array(catTrues == True)] = i
		i+=1
	return categ

def scoreClusters(predicted_clusters, labels_):
	labels_IX = labels_.index.values
	

	true_classes = labels_.ix[labels_IX]
	true_classes_array = np.squeeze(np.asarray(true_classes))
	
	print(completeness_score(true_classes_array,predicted_clusters))
	print(homogeneity_score(true_classes_array,predicted_clusters))

def performPCA():
	dataSet = pre.getDataFromCSV()
	data_ = dataSet.iloc[:,1:-1]
	labels_ = dataSet.iloc[:,-1]
	ids_ = dataSet.iloc[:,0]
	norm_data = pre.completePreprocessing(data_,data_)
	pca = PCA(n_components=5)
	pca_tracks = pca.fit(norm_data)
	pca_tracks_data = pca.transform(norm_data)
	print(pca_tracks.explained_variance_ratio_)
	myCluster(pca_tracks_data, labels_)



def getClusterSize(clusterNumber, clusterAssignment):
    clu = clusterAssignment[:,0] == clusterNumber
    cluSize = clu[clu==True].shape
    return cluSize

def cosine_similarity(vecA, vecB):
    D_norm = np.linalg.norm(vecA)
    x_norm = np.linalg.norm(vecB)
    sims = np.dot(vecA,vecB)/(D_norm * x_norm)
    return sims

def dist_i_cosine_similarity(vecA, vecB):
    sims = cosine_similarity(vecA,vecB)
    dist = 1 - sims
    return dist

def randCent(dataSet, k):
    n = np.shape(dataSet)[1]
    centroids = np.zeros((k,n), dtype=float)
    for j in range(n): #create random cluster centers
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = minJ + rangeJ * np.random.rand(k)
    return centroids 

def kMeans(dataSet, k, distMeas, createCent=randCent):
    m = np.shape(dataSet)[0]
    clusterAssment = np.zeros((m,2))#create mat to assign data points 
                                      #to a centroid, also holds SE of each point
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):#for each data point assign it to the closest centroid
            minDist = np.inf; minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        # print centroids
        for cent in range(k):#recalculate centroids
            ptsInClust = dataSet[np.nonzero(clusterAssment[:,0]==cent)[0]] #get all the point in this cluster - Note: this was incorrect in the original distribution.
            if(len(ptsInClust)!=0):
                centroids[cent,:] = np.mean(ptsInClust, axis=0) #assign centroid to mean - Note condition was added 10/28/2013
    return centroids, clusterAssment

# cluster()
# print("My Cluster")
# myCluster()
# performPCA()