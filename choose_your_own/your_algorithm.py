#!/usr/bin/python

from time import time
import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
import argparse

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

parser = argparse.ArgumentParser()
parser.add_argument('--plot', dest='plot', required=False, action='store_true')
parser.add_argument('--no-plot', dest='plot', required=False, action='store_false')
parser.set_defaults(plot=False)
args = parser.parse_args()

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]

#### initial visualization
print '*** INPUT DATA:'
print '* TRAINING set size: {0}'.format(len(features_train))
print '* TEST set size: {0}'.format(len(features_test))
print '* FEATURES size: {0}'.format(len(features_train[0]))
print '***'

plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
if args.plot: plt.show()
################################################################################

# Classifier Algorithms choices, as suggest by teachers
#
# 1. k nearest neighbors
# 2. random forest
# 3. adaboost (sometimes also called boosted decision tree)

### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary

classifiers = {
  'Gaussian Naive Bayes': GaussianNB(),
  'SVM (RBF kernel, C=10k)': SVC(kernel="rbf", C=10000.0),
  'Decision Tree (min sample split 40)': DecisionTreeClassifier(min_samples_split=40),
  'K-Nearest Neighbors (default)': KNeighborsClassifier(),
  'AdaBoost (default)': AdaBoostClassifier(),
  'AdaBoost (200 estimators)': AdaBoostClassifier(n_estimators=200),
  'Random Forest (default)': RandomForestClassifier(),
  'Random Forest (min sample split 40)': RandomForestClassifier(min_samples_split=40),
  'Random Forest (10 estimators, no max depth, min sample split 2)': RandomForestClassifier(n_estimators=10, max_depth=None, min_samples_split=2),
  'Extremely Randomized Trees (default)': ExtraTreesClassifier(),
  'Extremely Randomized Trees (min sample split 30)': ExtraTreesClassifier(min_samples_split=30),
  'Extremely Randomized Trees (10 estimators, no max depth, min sample split 2)': ExtraTreesClassifier(n_estimators=10, max_depth=None, min_samples_split=2)
}

for clfName, clf in classifiers.iteritems():
  print '*** {0} Classifier results:'.format(clfName)

  ### fit the classifier on the training features and labels
  fitTimeStart = time()
  clf.fit(features_train, labels_train)
  fitTimeEnd = time()

  ### calculate and return the accuracy on the test data
  scoreTimeStart = time()
  accuracy = clf.score(features_test, labels_test)
  scoreTimeEnd = time()

  print '  * Accuracy of {0}: {1}'.format(clfName, accuracy)
  print '  * TRAINING time ({0}.fit()): {1}s'.format(clfName, round(fitTimeEnd - fitTimeStart, 3))
  print '  * PREDICTION time ({0}.score()): {1}s'.format(clfName, round(scoreTimeEnd - scoreTimeStart, 3))
  print '***'

  try:
    prettyPicture(clf, features_test, labels_test)
    if args.plot: plt.show()
  except NameError:
    pass
