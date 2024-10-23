# Seaborn 

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# gapminder - pip install gapminder
from gapminder import gapminder # data set

# data
data = gapminder.loc[gapminder.year == 2007]
dataAll = gapminder
dataChina = gapminder.loc[gapminder.country == 'China']

# use the scatterplot function to build the bubble map
sns.scatterplot(data=data, x="gdpPercap", y="lifeExp", 
    size="pop", hue = "country", legend=False, sizes=(20, 2000)) # 
plt.show()

sns.scatterplot(data=data, x="gdpPercap", y="lifeExp", 
    size="pop", legend=False, sizes=(20, 2000))
plt.show()

sns.scatterplot(data=dataAll, x="gdpPercap", y="lifeExp", 
    size="pop", legend=False, hue = 'country', sizes=(20, 2000))
plt.show()

sns.scatterplot(data=dataChina, x="gdpPercap", y="lifeExp", 
    size="pop", legend=False, hue = 'year', palette='colorblind', sizes=(20, 2000))
plt.show()

sns.scatterplot(data=dataChina, x="gdpPercap", y="lifeExp", 
    size="pop", legend=False, hue = 'year', palette='mako', sizes=(20, 2000))
plt.show()

df_japan = gapminder.loc[gapminder.country == 'Japan']
sns.scatterplot(data=df_japan, x="gdpPercap", y="lifeExp", 
    size="pop", legend=False, hue = 'year', palette='mako', sizes=(20, 2000))
plt.show()


tips = sns.load_dataset("tips")
# regplot
sns.regplot(x="total_bill", y="tip", data=tips)
plt.show()

# Facet
g = sns.FacetGrid(tips, col="day", row="sex")
g.map_dataframe(sns.histplot, x="total_bill", binwidth=2, binrange=(0, 60))
plt.show()

# colormap example