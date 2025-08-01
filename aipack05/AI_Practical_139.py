#AIPractical_138

#Dropping missing values using dropna()
#-----------------------------------------

#In order to drop a null values from a dataframe, we used dropna() function
#This function drop Rows/Columns of datasets with Null values in different ways.

#Dropping rows with at least 1 null value.
import pandas as pd
import numpy as np
# dictionary of lists
dict = {'First Score':  [100, 90,     np.nan, 95, np.nan],
        'Second Score': [30,  np.nan, 45,     56, np.nan],
        'Third Score':  [52,  40,     80,     98, np.nan],
        'Fourth Score': [np.nan, np.nan, np.nan, 65, np.nan]
        }

# creating a dataframe from dictionary
df = pd.DataFrame(dict)
print( df )

#drop all rows that have any NaN values
df2 = df.dropna( )   #how='any'
print("\n\n", df2 )

#drop only if ALL columns are NaN
df3 = df.dropna(how='all')
print("df3 = \n", df3 )


#Drop row if it does not have at least three values that are not NaN
df4 = df.dropna(thresh=3)
print("df4 = \n", df4 )


#Drop only if NaN in specific column (as asked in the question)
df5 = df.dropna(subset=['Second Score'])
print("df5 = \n", df5 )