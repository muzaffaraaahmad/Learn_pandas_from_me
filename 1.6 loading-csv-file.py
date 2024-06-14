import pandas as pd


csv_path ="/Users/abc/Desktop/python/Pandas/Learn_pandas_from_me/Iris.csv"

#we can store the csv file in some dataframe df
df =pd.read_csv(csv_path)
print(type(df))


#syntax:

#pd.read_csv("file_path")




