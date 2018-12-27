import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score

def calculate_quality(clf):
    data_ = pd.read_csv('files/lesson_9/train.csv')
    X_train, X_test, y_train, y_test = train_test_split(data_.drop(['target','ID'], axis = 1), data_['target'], test_size=0.33, random_state=42)
    
    clf.fit(X_train, y_train)
    y_out = clf.predict(X_test)
    error = r2_score(y_test, y_out)                                
    print(str(error))