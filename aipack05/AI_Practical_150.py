#AIPractical150

#Filling null values in CSV File
import pandas as pd
# making data frame from csv file
data = pd.read_csv("employees_with_missing_data.csv")

# Printing the first 10 to 24 rows of the data frame for visualization
print("Original Data=\n", data[10:25] )
#Analyse the value of Gender in RowIndex no-20 and 22.
#Now we are going to fill all the null values in Gender column with “No Gender”

# filling a null values using fillna()
df2 = data["Gender"].fillna("No Gender")

#print( "\n\n\n", data )
print( "\n\n\n Data after filling = \n", df2[10:25] )