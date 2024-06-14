import pandas as pd


csv_path ="/Users/abc/Desktop/python/Pandas/Learn_pandas_from_me/Iris.csv"

#we can store the csv file in some dataframe df
df =pd.read_csv(csv_path)
print(df.shape)


#minimum
print(df.min())

#maximum
print(df.max())


#mean
print(df.mean())


#mean
print(df.median())
