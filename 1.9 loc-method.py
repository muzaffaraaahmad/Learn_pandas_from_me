# if we have a dataset(dataframe ) and i want to extract
# we use the  some information form that  we use loc[] method


##################################
##     loc[rows,column_name]       ## 
##################################


# here we are giving column names




import pandas as pd


csv_path ="/Users/abc/Desktop/python/Pandas/Learn_pandas_from_me/Iris.csv"

#we can store the csv file in some dataframe df
df =pd.read_csv(csv_path)


#if you want  from row 5 rows to row 9 and column 2 to column 4
df_new = df.loc[5:10,("SepalLengthCm","Species")]
print(df_new.head())