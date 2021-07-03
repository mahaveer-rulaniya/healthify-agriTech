import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import pickle

df = pd.read_csv('Life Expectancy Data.csv')
df.rename(columns = {" BMI " :"BMI",
                                  "Life expectancy ": "Life_expectancy",
                                  "Adult Mortality":"Adult_mortality",
                                  "infant deaths":"Infant_deaths",
                                  "percentage expenditure":"Percentage_expenditure",
                                  "Hepatitis B":"HepatitisB",
                                  "Measles ":"Measles",
                                  "under-five deaths ": "Under_five_deaths",
                                  "Total expenditure":"Total_expenditure",
                                  "Diphtheria ": "Diphtheria",
                                  " thinness  1-19 years":"Thinness_1-19_years",
                                  " thinness 5-9 years":"Thinness_5-9_years",
                                  " HIV/AIDS":"HIV/AIDS",
                                  "Income composition of resources":"Income_composition_of_resources"}, inplace = True)

y = df["Life_expectancy"]
df = df.drop(["Life_expectancy"], axis=1)

categorical = df.select_dtypes(include= "O")
numerical = df.select_dtypes(exclude= "O")


def outlier_count(col, data=df):
    print ( "\n" + 15 * '-' + col + 15 * '-' + "\n" )

    q75, q25 = np.percentile ( data[col], [75, 25] )
    iqr = q75 - q25
    min_val = q25 - (iqr * 1.5)
    max_val = q75 + (iqr * 1.5)
    outlier_count = len ( np.where ( (data[col] > max_val) | (data[col] < min_val) )[0] )
    outlier_percent = round ( outlier_count / len ( data[col] ) * 100, 2 )
    print ( 'Number of outliers: {}'.format ( outlier_count ) )
    print ( 'Percent of data that is outlier: {}%'.format ( outlier_percent ) )

def checkna(df):
    missing_values = df.isna().sum().reset_index()
    missing_values.columns = ["Features", "Missing_Values"]
    missing_values["Missing_Percent"]= round(missing_values.Missing_Values/len(df)*100,2)
    return missing_values[missing_values.Missing_Values > 0 ]


def imputer(df, feature, method):
    if method == "mode":
        df[feature] = df[feature].fillna ( df[feature].mode ()[0] )

    elif method == "median":
        df[feature] = df[feature].fillna ( df[feature].median () )

    else:
        df[feature] = df[feature].fillna ( df[feature].mean () )

features_missing= df.columns[df.isna().any()]
for feature in features_missing:
    imputer(df, feature= feature, method= "mean")

y.fillna(y.median(), inplace=True)

df['Status'] = df['Status'].replace({'Developed': 1 , 'Developing':0});

X = df.drop(['Country', 'Year', 'Infant_deaths'],1)




from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 42)

print(X_train.columns)
print(y_train)
from sklearn.ensemble import RandomForestRegressor
reg = RandomForestRegressor(n_estimators = 100, random_state = 0)
reg.fit(X_train, y_train)

pickle.dump(reg, open('model.pkl','wb'))

loaded_model = pickle.load(open('model.pkl','rb'))
result  = loaded_model.score(X_test, y_test)
print(result)