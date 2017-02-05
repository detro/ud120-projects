#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import tree

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

print 'Number of data points: {0}'.format(len(features_train))
print 'Number of features: {0}'.format(len(features_train[0]))

# Create Decision Tree classifier
clf = tree.DecisionTreeClassifier(min_samples_split=40)

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
print 'Accuracy of DecisionTree classifier: {0}'.format(accuracy)
print 'TRAINING time (DecisionTreeClassifier.fit()): {0}s'.format(round(fitTimeEnd - fitTimeStart, 3))
print 'PREDICTION time (DecisionTreeClassifier.score()): {0}s'.format(round(scoreTimeEnd - scoreTimeStart, 3))

#########################################################


