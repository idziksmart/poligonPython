import numpy as np
import pandas as pd

data = {'price': [108, 109, 110, 110, 109, np.nan, np.nan, 112, 111, 111]}
date_range = pd.date_range(start='01-01-2020 09:00', end='01-01-2020 18:00', periods=10)

df = pd.DataFrame(data=data, index=date_range)
print(df)


from pandas.plotting import register_matplotlib_converters
import matplotlib.pyplot as plt
import seaborn as sns
register_matplotlib_converters()
sns.set()

plt.figure(figsize=(10, 4))
plt.title('Braki danych')
_ = plt.plot(df.price)
# plt.show()

# wizualne interakcje
import plotly.express as px

df_plotly = df.reset_index()
fig = px.line(df_plotly, 'index', 'price', width=600, height=400,
        title='Szeregi czasowe - braki danych')
# fig.show()

# usuniecie brakow
df_plotly = df_plotly.dropna()
fig1 = px.line(df_plotly, 'index', 'price', width=600, height=400,
        title='Szeregi czasowe - braki danych')
# fig1.show()

# Wypełnienie braków stałą wartością 0

df_plotly = df.reset_index()
df_plotly['price_fill'] = df_plotly['price'].fillna(0)
fig2 = px.line(df_plotly, 'index', 'price_fill', width=600, height=400,
        title='Szeregi czasowe - braki danych - wstawienie 0')
# fig2.show()

# Wypełnienie braków średnią

df_plotly = df.reset_index()
df_plotly['price_fill'] = df_plotly['price'].fillna(df_plotly['price'].mean())
fig3 = px.line(df_plotly, 'index', 'price_fill', width=600, height=400,
        title='Szeregi czasowe - braki danych - wstawienie średniej')
# fig3.show()

# Zastosowanie interpolacji

df_plotly = df.reset_index()
df_plotly['price_fill'] = df_plotly['price'].interpolate()
fig4 = px.line(df_plotly, 'index', 'price_fill', width=600, height=400,
        title='Szeregi czasowe - braki danych - interpolacja')
# fig4.show()

# Wypełnienie braków metodą forward fill

df_plotly = df.reset_index()
df_plotly['price_fill'] = df_plotly['price'].fillna(method='ffill')
fig5 = px.line(df_plotly, 'index', 'price_fill', width=600, height=400,
        title='Szeregi czasowe - braki danych - forward fill')
# fig5.show()


# Wypełnienie braków metodą backward fill

df_plotly = df.reset_index()
df_plotly['price_fill'] = df_plotly['price'].fillna(method='bfill')
fig6 = px.line(df_plotly, 'index', 'price_fill', width=600, height=400,
        title='Szeregi czasowe - braki danych')
fig6.show()