"""
    classify flower images using multi-class SVM models with
    one-vs-all approach. The dataset consists images from 5 classes.
    0: Daisy, 1: Dandelion, 2: Rose, 3: Sunflower, 4: Tulip

    we will use two set of features
        - raw iamge pixels
        - features extracted from iamges by a deep convolutional 
        neural network
"""

from scipy.io import loadmat
import numpy as np
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

mat = loadmat('datasets/q4_dataset.mat')
inception_features = mat.get('inception_features')
images = mat.get('images')
class_labels = mat.get('class_labels')

parameters = [{
'kernel': ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed'], 
'C': [1,2,3,300,500],
'max_iter': [1000,100000]}]


clf = GridSearchCV(
        SVC(), parameters, scoring='accuracy'
    )

clf.fit(inception_features, class_labels)
print(clf.best_params_)
