#Filling a null values using replace() method

import pandas as pd
import numpy as np

# making data frame from csv file
data = pd.read_csv("employees_with_missing_data.csv")

# will replace  Nan value in dataframe with value -99
df2 = data.replace(to_replace=np.nan, value=-99)
print(df2)

df3 = df2.replace(to_replace='Male', value='M')
df4 = df3.replace(to_replace='Female', value='F')

print("-#-" * 30)
print(df4)