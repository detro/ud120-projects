#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

### create classifier
clf = GaussianNB()

### fit the classifier on the training features and labels
fitTimeStart = time()
clf = clf.fit(features_train, labels_train)
fitTimeEnd = time()

### calculate and return the accuracy on the test data
scoreTimeStart = time()
accuracy = clf.score(features_test, labels_test)
scoreTimeEnd = time()

print 'Feature TRAINING set size: {0}'.format(len(features_train))
print 'Feature TEST set size: {0}'.format(len(features_test))
print 'Accuracy of Gaussian Naive Bayes classifier: {0}'.format(accuracy)
print 'TRAINING time (GaussianNB.fit()): {0}s'.format(round(fitTimeEnd - fitTimeStart, 3))
print 'PREDICTION time (GaussianNB.score()): {0}s'.format(round(scoreTimeEnd - scoreTimeStart, 3))

#########################################################
