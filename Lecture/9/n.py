import os
from multiprocessing import Process
from threading import Thread
from multiprocessing import Lock
from time import sleep
import datetime
import urllib.request
from sklearn.metrics import  r2_score
from sklearn.model_selection import  train_test_split
import numpy as np
from sklearn import ensemble
from pandas import pd

def first():
    data_ = pd.read_csv('files/lesson_9/train.csv')
    y = data_.target
    X = data_.drop(['target', 'ID'], axis = 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    clf1 = ensemble.GradientBoostingRegressor()
    clf1.fit(X_train, y_train)
    print("R^2:", r2_score(y_test, clf1.predict(X_test)))
    
def second():
    data_ = pd.read_csv('files/lesson_9/train.csv')
    y = data_.target
    X = data_.drop(['target', 'ID'], axis = 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    clf1 = ensemble.RandomForestRegressor()
    clf1.fit(X_train, y_train)
    print("R^2:", r2_score(y_test, clf1.predict(X_test)))