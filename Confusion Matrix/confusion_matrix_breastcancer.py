# -*- coding: utf-8 -*-
"""Confusion_Matrix_BreastCancer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-ohqe7A1fp8cJljwbk33mPSyVNqTYqxG
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix,accuracy_score,precision_score,recall_score
from sklearn import svm,datasets
import matplotlib.pyplot as plt

# Import iris dataset
data_cancer = datasets.load_breast_cancer()
# 
X,y = data_cancer.data,data_cancer.target
# Split the dataset into training and test data
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=10)
print(X_test.shape)
# Define the classifier
classifier = svm.SVC(C=0.01,kernel='linear')
#Fit the classifier
classifier.fit(X_train,y_train)
# Plot the confusion matrix
display = plot_confusion_matrix(classifier,X_test,y_test,display_labels=data_cancer.target_names)
plt.show()
# Accuracy
print("Accuracy of the classifier:",accuracy_score(y_test,classifier.predict(X_test)))
print("Precision score is:", precision_score(y_test,classifier.predict(X_test),average=None))
print("Recall score is :",recall_score(y_test,classifier.predict(X_test),average=None))