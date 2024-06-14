# if we have a dataset(dataframe ) and i want to drop coulmn
#we use drop() method


#######################################
##   drop("colunm_name",axis=1)      ## 
#######################################




import pandas as pd


csv_path ="/Users/abc/Desktop/python/Pandas/Learn_pandas_from_me/Iris.csv"

#we can store the csv file in some dataframe df
df =pd.read_csv(csv_path)
print(df.shape)


#if you want to drop the colum species
df_new = df.drop("Species", axis=1)
print(df_new.head())
print(df_new.shape)