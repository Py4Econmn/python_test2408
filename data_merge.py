import pandas as pd

df = pd.read_excel("data/bop.xlsx")

df.columns = df.iloc[0]