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

def say_hello(name):
    print(os.getpid())
    print("hello", name)

	
class say_hello_class(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name
        
    def run(self):
        print(os.getpid())
        print("hello", self.name)	
		
class say_hello_class_T(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
        
    def run(self):
        print(os.getpid())
        print("hello", self.name)	
		
		
def count():
    data_ = pd.read_csv('files/lesson_9/train.csv')
    y = data_.target
    X = data_.drop(['target', 'ID'], axis = 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    clf1 = ensemble.GradientBoostingRegressor()
    clf1.fit(X_train, y_train)
    print("R^2:", r2_score(y_test, clf1.predict(X_test)))
    
def first(arg):
    data_ = pd.read_csv('files/lesson_9/train.csv')
    y = data_.target
    X = data_.drop(['target', 'ID'], axis = 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    clf1 = ensemble.GradientBoostingRegressor()
    clf1.fit(X_train, y_train)
    print("R^2:", r2_score(y_test, clf1.predict(X_test)))


def printer():
    data_ = pd.read_csv('files/lesson_9/train.csv')
    y = data_.target
    X = data_.drop(['target', 'ID'], axis = 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    clf1 = ensemble.RandomForestRegressor()
    clf1.fit(X_train, y_train)
    print("R^2:", r2_score(y_test, clf1.predict(X_test))) 		
		
		
def slow_print(s):
    print('Вызов {} в {}'.format(s, datetime.datetime.now()))
    sleep(1)
    print('Конец {} в {}'.format(s, datetime.datetime.now()))
	
def run(url):
    handle = urllib.request.urlopen(url)
    fname = os.path.basename(url)
    
    with open(fname, "wb") as f_handler:
        while True:
            chunk = handle.read(1024)
            if not chunk:
                break
            f_handler.write(chunk)
    msg = "%s has finished downloading %s" % (url)
		