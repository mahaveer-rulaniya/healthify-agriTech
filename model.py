import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

df = pd.read_csv('healthcare-dataset-stroke-data.csv')


# As 'id' Column is of no use. So, we drop that column
df = df.drop(['id'], 1)

df['bmi'] = df['bmi'].fillna(df['bmi'].median())

df_delete = df[df['gender'] == 'Other'].index
df = df.drop(df_delete)


X1 = df.iloc[:, :-1]
y = df.iloc[:, -1]

data = pd.get_dummies(X1);

X= data


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators= 100, criterion = 'gini' , random_state = 0)
classifier.fit(X_train, y_train)




pickle.dump(classifier, open('model.pkl','wb'))

loaded_model = pickle.load(open('model.pkl','rb'))
result  = loaded_model.score(X_test, y_test)
print(result)

print(X.shape)