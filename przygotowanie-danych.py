import numpy as np
# wizualizacje
import pandas as pd
# jest oparta o numpy
import sklearn as sk

# preprocessing

# wygenerowanie danych
# to jest dictionary pythona
data = {
    'size': ['XL', 'L', 'M', 'L', 'M'],
    'color': ['red', 'green', 'blue', 'green', 'red'],
    'gender': ['female', 'male', 'male', 'female', 'female'],
    'price': [199.0, 89.0, 99.0, 129.0, 79.0],
    'weight': [500, 450, 300, 380, 410],
    'bought': ['yes', 'no', 'yes', 'no', 'yes']
}

df_raw = pd.DataFrame(data=data)

# utworzenie kopii
df = df_raw.copy()

# wyswietlenie podstawowych informacji
# df.info()

# zmiana typu danych
for col in ['size', 'color', 'gender', 'bought']:
    df[col] = df[col].astype('category')
df['weight'] = df['weight'].astype('float')
# df.info()

# statystyki tylko dla kolumn numerycznych
print(df.describe())
print(df.describe().T)

# dodanie pewnych statystyk na temat zmiennych kategorycznych (dodajemy typ kolumny)
print(df.describe(include=['category']).T)

# kodowanie
# bedziemy przygotowywali obiekt do modelu uczenia maszynowego

# mapowanie bought na wartosci logiczne
from sklearn.preprocessing import LabelEncoder

#  przeksztalcanie tylko dla zmniennych docelowych (dobra praktyka by nie uzywac jej do zmiennych kategorycznych)
le = LabelEncoder()
#  dopasowanie encodera do zmiennej
le.fit(df['bought'])
# transformowanie naszych danych
print(le.transform(df['bought']))

# albo w jednej metodzie
print(le.fit_transform(df['bought']))

# jak to mapowanie wyglada
print(le.classes_)

# przekazanie obiektu do modelu
df['bought'] = le.fit_transform(df['bought'])
print(df)

# powrot do poprzedniej postaci
df['bought'] = le.inverse_transform(df['bought'])

# przeksztalcanie zmiennych kategorycznych
from sklearn.preprocessing import OneHotEncoder

# false, bo domyslnie klasa zwraca macierz rzadką (trzymanie w pamieci wystapien pozycji dla np 1)
encoder = OneHotEncoder(sparse_output=False)
encoder.fit(df[['size']])
print(encoder.transform(df[['size']]))
print(encoder.categories_)

# jednak jest tutaj liniowa zaleznosc a tak nie powinno byc a wiec przekazujemy parametr drop=first ktory usuwa pierwsza z kolumn
encoder = OneHotEncoder(drop='first', sparse_output=False)
encoder.fit(df[['size']])
print(encoder.transform(df[['size']]))
print(encoder.categories_)

# z getDummies jest lepiej korzystać niż z OneHotEncoder
print(pd.get_dummies(data=df))
print(pd.get_dummies(data=df, drop_first=True))
print(pd.get_dummies(data=df, drop_first=True, prefix="my"))
print(pd.get_dummies(data=df, drop_first=True, prefix_sep="-"))
print(pd.get_dummies(data=df, drop_first=True, columns=['size', 'gender']))

# standaryzacja danych (skala nie ma zmaczenia, ale wariancja)
# zmienne numeryczne StandardScaler
# odchylenie standardowe jest estymatorem obciazonym wariancji
# w pandas jest zaimplementowany nieobciazony estymator wariancji std()
# w numpy jest zaimplementowany obciazony estymator wariancji std()
# przy obliczeniu odchylenia sandardowego i wariancji moge wychodzic inne wyniki

# w pandas
print(f"{df['price']}\n")
print(f"Srednia {df['price'].mean()}\n")
print(f"Odchylenie {df['price'].std()}\n")

# standaryzacja to odjecie sredniej od wartosci i podzielenie przez odchylenie standardowe
print((df['price'] - df['price'].mean()) / df['price'].std())

# a jak to wyglada w sci learn? jest metoda scale()
from sklearn.preprocessing import scale
print(scale(df['price']))

# lepsza bedzie klasa StandardScaler (daje te same wyniki). ktora pozwala zachowac ustawienia w przypadku pojawienia sie nowych danych
from sklearn.preprocessing import StandardScaler

scaler_price = StandardScaler()
print(scaler_price.fit_transform(df[['price']]))
scaler_weight = StandardScaler()
print(scaler_weight.fit_transform(df[['weight']]))

# dwie kolmny na raz
scaler = StandardScaler()
df[['price', 'weight']] = scaler.fit_transform(df[['price', 'weight']])
print(df)

# od poczatku, podsumowanie
df = df_raw.copy()
le = LabelEncoder()
df['bought'] = le.fit_transform(df['bought'])
scaler = StandardScaler()
df[['price', 'weight']] = scaler.fit_transform(df[['price', 'weight']])
df = pd.get_dummies(data=df, drop_first=True)
print(df)