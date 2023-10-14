import numpy as np
import pandas as pd
import sklearn


def fetch_financial_data(company='AMZN'):
    """
    This function fetches stock market quotations.
    """
    import pandas_datareader as web
    return web.DataReader(name=company, data_source='stooq')

df_raw = fetch_financial_data()
print(df_raw.head())


# wyciecie pierwszych 5ciu wierszy
df = df_raw.copy()
df = df[:5]
print(df.info())

# generowanie nowych zmiennych

df.index.month
df['day'] = df.index.day
df['month'] = df.index.month
df['year'] = df.index.year
df

# Dyskretyzacja zmiennej ciągłej (przedstawienie jako zmiennej kategorycznej)
df = pd.DataFrame(data={'height': [175., 178.5, 185., 191., 184.5, 183., 168.]})

# bins - liczba przedzialow
df['height_cat'] = pd.cut(x=df.height, bins=3)
df['height_cat'] = pd.cut(x=df.height, bins=(160, 175, 180, 195))
df['height_cat'] = pd.cut(x=df.height, bins=(160, 175, 180, 195), labels=['small', 'medium', 'high'])
pd.get_dummies(df, drop_first=True, prefix='height')

# ekstrakcja cech
df = pd.DataFrame(data={'lang': [['PL', 'ENG'], ['GER', 'ENG', 'PL', 'FRA'], ['RUS']]})
df['lang_number'] = df['lang'].apply(len)
df['PL_flag'] = df['lang'].apply(lambda x: 1 if 'PL' in x else 0)

df = pd.DataFrame(data={'website': ['wp.pl', 'onet.pl', 'google.com']})
df.website.str.split('.', expand=True)
new = df.website.str.split('.', expand=True)
df['portal'] = new[0]
df['extension'] = new[1]