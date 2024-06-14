# if you want to half of the value of some columns, 
# we use apply method

import pandas as pd


csv_path ="/Users/abc/Desktop/python/Pandas/Learn_pandas_from_me/Iris.csv"

#we can store the csv file in some dataframe df
df =pd.read_csv(csv_path)
print(df.shape)



#if we have categorical column and want to know how 
# how many we use value_counts()
c= df["Species"].value_counts()
print(c)