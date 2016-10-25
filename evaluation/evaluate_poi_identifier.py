#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from time import time

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)


### your code goes here 
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features,labels, test_size=0.3, random_state=42)

from sklearn import tree
clf = tree.DecisionTreeClassifier()
t0 = time()
clf = clf.fit(features_train, labels_train)
#clf = clf.fit(features, labels)

print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
#pred = clf.predict(features)
print "prediction time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score
print accuracy_score(pred, labels_test)
#print accuracy_score(pred, labels)

count = 0
for i,j in zip(pred, labels_test):
    if i == j and i == 1.0:
        temp = "true positive"
        count = count + 1
    else:
        temp = ""
    print i," / ",j, " / ",temp       
        
print "######################################################"

from sklearn import metrics
y_true = labels_test
y_pred = pred

recall = metrics.recall_score(y_true,y_pred,average='macro')
print "recall:",recall

precision = metrics.precision_score(y_true,y_pred,average='macro')
print "precision:",precision

print "######################################################"

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]  
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

count = 0
for i,j in zip(predictions, true_labels):
    if i == 1.0 and j == 1.0:
        temp = "true positive"
        count = count + 1
    else:
        temp = ""
#    print i," / ",j, " / ",temp 
    
true_positives = count
print "true positives:",count
    
print "######################################################"   

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]  
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

count = 0
for i,j in zip(predictions, true_labels):
    if i == j and i == 0.0:
        temp = "true negative"
        count = count + 1
    else:
        temp = ""
#    print i," / ",j, " / ",temp  

true_negatives = count
print "true negatives:",count
    
print "######################################################"    
    
predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]  
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

count = 0
for i,j in zip(predictions, true_labels):
    if i == 1.0 and j == 0.0:
        temp = "false positive"
        count = count + 1
    else:
        temp = ""
#    print i," / ",j, " / ",temp  

false_positives = count
print "false positives:",count
    
print "######################################################"

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]  
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

count = 0
for i,j in zip(predictions, true_labels):
    if i == 0.0 and j == 1.0:
        temp = "false negative"
        count = count + 1
    else:
        temp = ""
#    print i," / ",j, " / ",temp
    
false_negatives = count    
print "false negatives:",count
    
print "######################################################"

precision = 1.0*true_positives/(true_positives+false_positives)
recall = 1.0*true_positives/(true_positives+false_negatives)
F1 = 2.0*(precision*recall)/(precision+recall)

print "precision:",precision
print "recall:",recall
print "F1:",F1

print "######################################################"

