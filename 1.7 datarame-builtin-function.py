import pandas as pd


csv_path ="/Users/abc/Desktop/python/Pandas/Learn_pandas_from_me/Iris.csv"

#we can store the csv file in some dataframe df
df =pd.read_csv(csv_path)



#first 5 rows of the dataframe
print(df.head())

print(30*"-")


#last 5 rows of the dataframe
print(df.tail())

print(30*"-")


#number of rows and number of columns in dataframe
print(df.shape)

print(30*"-")



#general method to discribe the full datafram
print(df.describe())

print(30*"-")

