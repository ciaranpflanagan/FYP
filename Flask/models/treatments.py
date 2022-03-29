import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


df_2021 = pd.read_csv('./../data/2021.csv')
treatment_definitions = pd.read_csv('./../data/Plough & Till Plan/Definitions.csv')
del treatment_definitions['Unnamed: 3']
del treatment_definitions['Unnamed: 4']

df_2021['ploughed'] = 0
df_2021['tilled'] = 0
df_2021['high pressure'] = 0
df_2021['low pressure'] = 0
df_2021['high moisture'] = 0
df_2021['low moisture'] = 0
df_2021['covercrop'] = 0
df_2021['no covercrop'] = 0
df_2021['high traffic'] = 0
df_2021['low traffic'] = 0

for index, row in treatment_definitions.iterrows():
    if 'Plough' in row['Description']:
        df_2021.at[index, 'ploughed'] = 1
    if 'Min Till' in row['Description']:
        df_2021.at[index, 'tilled'] = 1
    if 'low pressure' in row['Description']:
        df_2021.at[index, 'low pressure'] = 1
    if 'high pressure' in row['Description']:
        df_2021.at[index, 'high pressure'] = 1
    if 'low moisture' in row['Description']:
        df_2021.at[index, 'low moisture'] = 1
    if 'high moisture' in row['Description']:
        df_2021.at[index, 'high moisture'] = 1
    if '3 Pass' in row['Description']:
        df_2021.at[index, 'high traffic'] = 1
    if '1 Pass' in row['Description']:
        df_2021.at[index, 'low traffic'] = 1

    # Cover crop is a special case, because "cover crop" is also a substring of "no cover crop"
    # we need to check "no cover crop" first, then if not found set 'covercrop' as true
    if 'no cover crop' in row['Description']:
        df_2021.at[index, 'no covercrop'] = 1
    else:
        df_2021.at[index, 'covercrop'] = 1

y = df_2021['Combine Yield (t/ac)']
y = y.fillna(0)
del df_2021['Combine Yield (t/ac)']

X = df_2021[['ploughed', 'tilled', 'high pressure', 'low pressure', 'high moisture', 'low moisture', 'covercrop', 'no covercrop', 'high traffic', 'low traffic']]
X = X.fillna(0)

# Splitting data for training & testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

def regYield(data):
    reg = LinearRegression().fit(X_train, y_train)

    return reg.predict(data)

def regEmergence(data):
    reg = LinearRegression().fit(X_train, y_train)

    return reg.predict(data)