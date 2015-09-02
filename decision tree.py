#!/usr/bin/python


"""
    starter code for the validation mini-project
    the first step toward building your POI identifier!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn import tree
from sklearn import cross_validation

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. 
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

# Cross validation set-up

X_train, X_test, y_train, y_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

# Create a decision tree

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

# print accuracy

print "Accuracy: " + str(clf.score(X_test, y_test))


