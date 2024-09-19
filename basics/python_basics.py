import datetime as dt

# Variable types
# integer
a = 5
type(a) 
type(a) == int

# float 
b = 5.0
type(b)
type(b) == float

# string
c = 'hello'
cc = "hello"
type(c)

c + ' ' + cc
c + '/' + cc

# boolean
True = 10
False

5 > 10
5 < 10
5 == 10

5 > 10 and 5 < 10
5 > 10 or 5 < 10
# 5 > 10 xor 5 < 10
d = True

# list
mlist = [5,2,3.0,4,5]
mmlist = ['bat',2,3,4,5]

mlist[0]
mlist[1]
mlist[0:3]
mlist[:3]
mlist[2:]
mlist[2:4]
mlist[2:-1]
mlist[2:-2]

mmlist[0] = 'bold'

mlist + mmlist
mlist + [6]
mlist.append(6)
mlist.append([2,3])
mlist.extend([2,3])

del mlist[-3]

# tuple
mtuple = (5,2,3.0,4,5)
new_tuple = mtuple + (4,)
mtuple = mtuple + (4,)

# dictionary 
john_dict = {'name':'John', 'age':25}
jane_dict = {'name':'Jane', 'age':23}

human = {'John':john_dict, 'Jane':jane_dict}
human['John']['name']
human['John']['age']


# dataframe
import pandas as pd

df = pd.DataFrame()
df['name'] = ['John', 'Jane']
df['age'] = [23, 25]

df = pd.DataFrame({'name':['John', 'Jane'], 'age':[23, 25]})

human = {'John':john_dict, 'Jane':jane_dict}
df = pd.DataFrame(human).T

bbsb = []
bbsb1 = [1,'BBSB1','2012']
bbsb2 = [2,'BBSB2','2007']

bbsb.append(bbsb1)
bbsb.append(bbsb2)

df = pd.DataFrame(bbsb, columns=['id','name','year'])


for i in range(100):
    print(i)

numlist = []
for i in range(100):
    q = i**2 + i*5 + 3
    c = i**3 + i*5 + 3
    st = f' {i} '
    numlist.append([i, q, c, st])

df = pd.DataFrame(numlist, columns=['num','num2','num3', 'st'])

for index, row in df.iterrows():
    print(f"Index: {index}")
    print(f"Row values: {row['num2']}, {row['num3']}")

df['string'] = df['num2'].astype(str) + ' ' + df['num3'].astype(str)

df.columns
df.info()
df.dtypes
df.describe()


# convert string column to integer
df['st_num'] = pd.to_numeric(df['st'])
df['st_num'] = df['st'].astype(int)
#  df['st'].str.strip().astype(int)

df = pd.read_excel('basics/datetime.xlsx') 

dt.date.today()
dt.date.today().year
dt.date.today().month
dt.date.today().day
dt.date.today().weekday()

dt.datetime.now()
dt.datetime.now().year
dt.datetime.now().hour
dt.datetime.now().second

mydt = dt.datetime(2024, 7, 11)
mydate = dt.date(2024, 7, 11)

# convert string to datetime - strptime
# https://www.w3schools.com/python/gloss_python_date_format_codes.asp
datestr = '20240711'
mydatestr = dt.datetime.strptime(datestr, '%Y%d%m')
mydatestr = dt.datetime.strptime('24-07-11', '%y-%m-%d')
dt.datetime.strptime('24 Aug 11', '%y %b %d')

# convert datetime to string - strftime
dt.datetime.strftime(mydatestr, '%Y---%d---%B---%H')
dt.datetime.strftime(mydatestr, '%Y-%B-%d-%H-%M-%S')  
dt.datetime.strftime(dt.datetime.now(), '%Y-%B-%d-%H-%M-%S')    

df['date3'] = pd.to_datetime(df['date2'], format='%Y%m%d')
df['date4'] = df['date3'].dt.strftime('%Y+%m+%d')


# timestamp
ts_now = dt.datetime.now().timestamp()
# timestamp of 2021-07-11
ts1 = dt.datetime(2021, 7, 11).timestamp()
ts2 = dt.datetime(2021, 7, 12).timestamp()

dt0 = dt.datetime.fromtimestamp(0)

