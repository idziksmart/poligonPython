import numpy as np
import pandas as pd
import sklearn as sk

data = {
    'size': ['XL', 'L', 'M', np.nan, 'M', 'M'],
    'color': ['red', 'green', 'blue', 'green', 'red', 'green'],
    'gender': ['female', 'male', np.nan, 'female', 'female', 'male'],
    'price': [199.0, 89.0, np.nan, 129.0, 79.0, 89.0],
    'weight': [500, 450, 300, np.nan, 410, np.nan],
    'bought': ['yes', 'no', 'yes', 'no', 'yes', 'no']
}

df_raw = pd.DataFrame(data=data)
df = df_raw.copy()
print(df.info())

# sprawdzenie brakow
print(df.isnull())
print(df.isnull().sum())
print(df.isnull().sum().sum())

# procentowo
print(df.isnull().sum()/len(df))

# uzupelnianie brakow danych - SimpleImputer

from sklearn.impute import SimpleImputer

# strategy: 'mean', 'median', 'most_frequent', 'constant'
# uzupelnienie srednia arytmetyczna
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(df[['weight']])

print(imputer.statistics_)

df['weight'] = imputer.transform(df[['weight']])
print(df)

# uzupelnianie stala wartoscia
imputer = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=99.0)
imputer.fit_transform(df[['price']])

imputer = SimpleImputer(missing_values=np.nan, strategy='constant', fill_value='L')
imputer.fit_transform(df[['size']])

# wstawienie najczescie wystepujacego elementu
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imputer.fit_transform(df[['size']])

df = df_raw.copy()

# filtrowanie
pd.isnull(df['weight'])

df[pd.isnull(df['weight'])]
df[~pd.isnull(df['weight'])]
pd.notnull(df['weight'])
df[pd.notnull(df['weight'])]

#
df.fillna(value='brak')
df.fillna(value=0.0)
df['size']

# true bo zmiany beda wykonane od razu na kolumnie
df['size'].fillna(value='L', inplace=True)

# usuwanie wierzy z brakami danych
df.dropna()
