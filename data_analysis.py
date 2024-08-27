import pandas as pd

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