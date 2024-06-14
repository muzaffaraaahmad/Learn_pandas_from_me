#creating dataframe from dictionary
import pandas as pd
s4 = pd.DataFrame({"Name":["muzi","fara","majid"],"Marks":[1,2,3]})
print(s4)

s5 =s4.set_index("Marks")
print(s5)