import pandas as pd
import numpy as np
import pickle

df=pd.read_csv('heart.csv')
x= df.iloc[:, :-1].values
y= df.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(x,y, test_size=0.3, random_state=100)

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier(n_estimators=120, random_state =100, criterion ='entropy')
model1=rfc.fit(X_train, y_train)

pickle.dump(model1,open('heart.pkl','wb'))