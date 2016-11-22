import numpy as np
import pandas as pd
from sklearn import neighbors, tree, naive_bayes
from sklearn import cross_validation
import Preprocessing as pre
from sklearn.lda import LDA

def excKNN(k, train_data, train_labels, test_data, test_labels):
    errorCount = 0.0
    knnclf = neighbors.KNeighborsClassifier(k, weights='distance')
    knnclf.fit(train_data, train_labels)
    numTestVecs = test_data.shape[0]
    for i in range(numTestVecs):
        classifierResult = knnclf.predict(test_data[i,:].reshape(1,-1))
#         print("the classifier came back with: ", classifierResult ,", the real answer is: " , bank_test_labels_arr[i])
        if (classifierResult != test_labels[i]):
            errorCount += 1.0
    print("the total error rate is: %f",errorCount / float(numTestVecs))

def startClassifyKNN():
	dataSet = pre.getDataFromCSV()
	train_data, train_labels, train_ids, test_data, test_labels, test_ids = sep_train_test(dataSet)

	train_norm = pre.completePreprocessing(train_data,train_data)
	test_norm = pre.completePreprocessing(train_data, test_data)

	knnclf = neighbors.KNeighborsClassifier(5, weights='distance')
	knnclf.fit(train_norm, train_labels)
	trainScore = knnclf.score(train_norm, train_labels)
	testScore = knnclf.score(test_norm, test_labels)
	print(trainScore)
	print(testScore)
	

def startClassifyTree():
	dataSet = pre.getDataFromCSV()
	train_data, train_labels, train_ids, test_data, test_labels, test_ids = sep_train_test(dataSet)
	treeclf = tree.DecisionTreeClassifier(criterion='entropy')
	treeclf = treeclf.fit(np.array(train_data), np.array(train_labels))
	print(treeclf.score(train_data, train_labels))
	print(treeclf.score(test_data, test_labels))

def test(cv=30):
	dataSet = pre.getDataFromCSV()
	data_ = dataSet.iloc[:,1:-1]
	labels_ = dataSet.iloc[:,-1]
	ids_ = dataSet.iloc[:,0]

	data_norm = pre.completePreprocessing(data_,data_)

	knnclf = neighbors.KNeighborsClassifier(5, algorithm='brute')
	scores_KNN = cross_validation.cross_val_score(knnclf, data_norm, labels_, cv=cv)
	print("Overall Accuracy: %0.2f (+/- %0.2f)" % (scores_KNN.mean(), scores_KNN.std() * 2))

	treeclf = tree.DecisionTreeClassifier(criterion='entropy')
	scores_ = cross_validation.cross_val_score(treeclf, np.array(data_), np.array(labels_), cv=cv)
	print("Overall Accuracy: %0.2f (+/- %0.2f)" % (scores_.mean(), scores_.std() * 2))

	# nbclf = naive_bayes.GaussianNB()
	# nbclf = nbclf.fit(data_norm, np.array(labels_))
	# scores_NB = cross_validation.cross_val_score(knnclf, data_norm, labels_, cv=cv)
	# print("Overall Accuracy: %0.2f (+/- %0.2f)" % (scores_NB.mean(), scores_NB.std() * 2))

	# # # #LDA
	# lda_cl = LDA()
	# lda_cl = lda_cl.fit(data_norm, labels_)
	# scores_LDA = cross_validation.cross_val_score(knnclf, data_norm, labels_, cv=cv)
	# print("Overall Accuracy: %0.2f (+/- %0.2f)" % (scores_LDA.mean(), scores_LDA.std() * 2))


def sep_train_test(dataSet, percent_test_cases=0.20):
	random_data_set = dataSet.reindex(np.random.permutation(dataSet.index))
	number_test_cases = int(random_data_set.shape[0]*percent_test_cases)

	test_data = random_data_set.iloc[:number_test_cases,1:-1]
	test_labels = random_data_set.iloc[:number_test_cases,-1]
	test_ids = random_data_set.iloc[:number_test_cases,0]

	train_data = random_data_set.iloc[number_test_cases:,1:-1]
	train_labels = random_data_set.iloc[number_test_cases:,-1]
	train_ids = random_data_set.iloc[number_test_cases:,0]

	return train_data, train_labels, train_ids, test_data, test_labels, test_ids

# startClassifyKNN()
# startClassifyTree()
test()
