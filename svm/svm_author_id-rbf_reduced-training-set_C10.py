#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

# Create SVM C-Support Vector Classification classifier
clf = SVC(kernel="rbf", C=10.0)

# OPTIONAL training set reduction (1% of the original set)
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

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
print 'Accuracy of C-SVC classifier: {0}'.format(accuracy)
print 'TRAINING time (SVC.fit()): {0}s'.format(round(fitTimeEnd - fitTimeStart, 3))
print 'PREDICTION time (SVC.score()): {0}s'.format(round(scoreTimeEnd - scoreTimeStart, 3))

#########################################################


