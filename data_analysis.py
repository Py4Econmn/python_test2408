import pandas as pd
import plotly.express as px

df = pd.read_excel("data/bop.xlsx", skiprows=1)

# columns
df.columns

# see variables
df['Индикатор нэр']
df['Индикатор нэр'].values

# see multiple columns
df[['Индикатор нэр', '2020-01 Эцсийн**', '2020-02 Эцсийн**']]

# head and tail
df.head()
df.tail()

# descriptive statistics
df.describe()

# info
df.info()
df.dtypes

# check for missing values
df.isnull()
df.isnull().sum()
df.isnull().sum(axis=1)

# change index
df.index
df.set_index("Индикатор нэр", inplace=True)


# transpose
df = df.T

# extract year and month
df['year'] = df.index.str[:4]
df['month'] = df.index.str[5:7]
df['date'] = df['year'].str[2:] + 'M' + df['month']

df.set_index('date', inplace=True)

keepvars = ['I. УРСГАЛ ДАНС','II. ХӨРӨНГИЙН ДАНС','III. САНХҮҮГИЙН ДАНС',
            'Төлбөрийн тэнцлийн нийт дүн','V. НӨӨЦ ХӨРӨНГӨ','IV. Алдаа болон орхигдуулга']

df = df[keepvars]
# df.columns = ['ca','cap','fa','bop','res','eo']

columns_dict = {
    'I. УРСГАЛ ДАНС' : 'ca',
    'II. ХӨРӨНГИЙН ДАНС' : 'cap',
    'III. САНХҮҮГИЙН ДАНС' : 'fa',
    'Төлбөрийн тэнцлийн нийт дүн' : 'bop',
    'V. НӨӨЦ ХӨРӨНГӨ' : 'res',
    'IV. Алдаа болон орхигдуулга' : 'eo'
}

df.rename(columns=columns_dict, inplace=True)

# Chart

fig = px.line(df, x=df.index, y='ca', title='Current account', markers=True)

# Show the plot
fig.show()