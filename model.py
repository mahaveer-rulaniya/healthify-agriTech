import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

df = pd.read_csv('Fertilizer Prediction.csv')

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X= X.drop(['Potassium'], axis = 1)

y = y.replace({'20-20':'20-20 Fertilizer (Ammonium Phosphate Sulphate)', '28-28':'Gromor 28-28 Fertilizer','14-35-14 ':'GROMOR 14-35-14 Fertilizer',
               '17-17-17':'NPK 17-17-17 Fertilizer', '10-26-26':'Water Soluble NPK 10:26:26 Fertilizer'})

data = pd.get_dummies(X)
X = data



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators= 100, criterion = 'gini' , random_state= 42)
classifier.fit(X_train, y_train)

pickle.dump(classifier, open('model.pkl','wb'))

loaded_model = pickle.load(open('model.pkl','rb'))
result  = loaded_model.score(X_test, y_test)
print(result)