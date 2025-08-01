#AIPractical_140
#Display only those rows which are having Gender = NULL.

import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_column', None)
pd.set_option('display.width', 1000)
# making data frame from csv file
data = pd.read_csv("employees_with_missing_data.csv")

# creating bool series True for NaN values
#bool_series = pd.isnull(data["Gender"])
bool_series = data["Gender"].isnull()
print(bool_series)

# filtering data
# displaying data only with Gender = NaN
result = data[bool_series]
print(result)
print(result.shape)
print(result.info() )


# filter data having gender not null
bool_series1 = data["Gender"].notnull()
print(bool_series1)

# filtering data
# displaying data only with Gender = NaN
result1 = data[bool_series1]
print(result1)
print(result1.shape)
print(result1.info() )