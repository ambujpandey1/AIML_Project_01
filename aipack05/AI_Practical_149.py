#AIPractical_149

#Display only those rows which are having Gender = NOT NULL.

import pandas as pd

# making data frame from csv file
data = pd.read_csv("employees_with_missing_data.csv")

# creating bool series True for NaN values
#bool_series = pd.notnull(data["Gender"])
bool_series = data["Gender"].notnull()

# filtering data
df2 = data[bool_series]

# displayind data only with Gender = Not NaN
print( df2 )