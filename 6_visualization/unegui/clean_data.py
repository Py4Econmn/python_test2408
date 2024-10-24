import re
import pandas as pd
import numpy as np
import os


name_cols = {'date_collect' : 'date_ind',
            'Title' : 'title',
            'Price' : 'price_total',
            'Date'  : 'date',
            'Time'  : 'time',
            'id'    : 'ad_id',
            'room'  : 'room_num',
            'loc'   : 'location',
            'message' : 'ad_text',
            'Шал:'  : 'floor_type',
            'Тагт:' : 'balcony_num',
            'Ашиглалтанд орсон он:' : 'date_op',
            'Гараж:': 'garage',
            'Цонх:' : 'window_type',
            'Барилгын давхар:' : 'floor_num',
            'Хаалга:' : 'door_type',
            'Талбай:' : 'size',
            'Хэдэн давхарт:'         : 'floor_at',
            'Төлбөрийн нөхцөл:' : 'leasing',
            'Цонхны тоо:'            : 'window_num',
            'Барилгын явц:'          : 'progress_cons',
            'Цахилгаан шаттай эсэх:' : 'elevator',
            }

def get_district(x):
    try:
        x = re.findall('(Баянгол|Баянзүрх|Сүхбаатар|Сонгинохайрхан|Хан-Уул|Чингэлтэй|Налайх)', x)[0]
    except:
        x = 'province'
    return x


# Load the data
df = pd.read_csv('6_visualization/unegui/data/daily.csv')
# df = df.iloc[:,:23]
df_loc = pd.read_csv('6_visualization/unegui/data/location.csv')

# Rename the columns
df.rename(columns=name_cols,inplace=True)

# Check for missing values
df.isna().sum() # axis=0 by column
df[df['ad_text'].isna()]['ad_text'].unique()
df[df.isna().sum(axis=1)>0] # by row
# df.dropna(subset=['ad_text'])

# Drop duplicates
df.drop_duplicates(subset=['date','time','ad_id'], keep='first', inplace=True)
# df[(df.duplicated(subset=['ad_id'],keep=False)) & (df['ad_id'] == 8199882)] # check for duplicates
# df[df['ad_id'] == 8199882]

## Date
df['date'] = pd.to_datetime(df['date'],format='mixed') # convert to datetime
np.sort(df['date'].unique())
df.groupby('date')['ad_id'].count()


df['weekday'] = df['date'].dt.strftime('%a')
df['hour'] = df['time'].apply(lambda x: int(x.split(':')[0]))
df.groupby('hour')['ad_id'].count()

# number of ads by hour and weekday
df.pivot_table(index='hour', columns='weekday', values='ad_id', aggfunc='count',margins=True)


## AREA
df['area'] = df['size'].apply(lambda x: re.findall('\d+[.\d]*', x)[0]).astype(float)

a_int = [-np.inf,15,30,50, 80,100,200,500,np.inf]
df['a_int'] = pd.cut(df['area'], bins=a_int, include_lowest=True)
df['a_int'].value_counts().sort_values()
df[df['area']>500][['size','area','a_int']]

df = df[~(df['area']>500) & ~(df['area']<15)] # remove outliers, area > 500



## PRICE
# remove text from price_total 
df = df[~df['price_total'].isna()]
df['price'] = df['price_total'].apply(lambda x: re.findall('\d+[.\d]*', x)[0]).astype(float) 

# convert price to million, from billion
mask = (df['price_total'].str.contains('бум', na=False)) & (df['price'] < 5)
df.loc[mask, 'price'] = df.loc[mask, 'price'] * 1000

df = df[~(df['price'] < 50) | ~(df['price'] > 20)] # remove outliers, price < 50 and price > 12

# price per m2
df['price_m2'] = df['price']

# no price m2 above 12, if larger than 12, then divide by area
mask = df['price'] > 20
df.loc[mask, 'price_m2'] = df.loc[mask, 'price'] / df.loc[mask, 'area'] 
df = df[df['price_m2'] > 1]
df = df[df['price_m2'] < 20]

## LOCATION
df['district'] = df['location'].apply(get_district)
df = df.merge(df_loc, on='location', how='left')

df[df['mylocation'].isna()][['location','mylocation']]
# df[df['mylocation'].isna()].to_csv('6_visualization/unegui/data/location_missing.csv',index=False,encoding='utf-8-sig')

df.to_csv('6_visualization/unegui/data/daily_cleaned.csv',index=False,encoding='utf-8-sig')