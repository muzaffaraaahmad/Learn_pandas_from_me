#series object: is a 1D labelled array

import pandas as pd
s1=pd.Series([1,2,3,4])
print(s1)
print(type(s1))


#we can give the index as well
s2=pd.Series([1,2,3,4], index=["a","b","c","d"])
print(s2)


#create object from dictionary

s3 = pd.Series({"a":10, "b":20, "c": 30})
print(s3)


#changing index for s3
s4 = pd.Series({"a":10, "b":20, "c": 30}, index=["b","c","d","a"])
print(s4)
