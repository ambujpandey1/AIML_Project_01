'''
MLProject Cab Ride Price Prediction
==================================
Assignment Part-01: Import Libraries
Question: Which libraries are imported for data manipulation, visualization, and machine learning?

Assignment Part-02: Configure Pandas Display
Question: How would you configure pandas to display all rows/columns and set the display width to 1000?

Assignment Part-03: Load Data
Question: Write code to load a CSV dataset named rideshare_dataset.csv into a variable of DataFrame named as 'data'.

Assignment Part-04: Create DataFrame Copy
Question: How do you create a new duplicate working copy of a DataFrame 'data' to 'df'?

Assignment Part-05: Inspect Missing Values
Question: How would you check for missing values in each column of df?

Assignment Part-06: Handle Missing Values
Question: Write code to drop rows with missing values specifically in the price column.

Assignment Part-07: Drop Irrelevant Columns
Question: Remove columns ['id', 'latitude', 'longitude', 'product_id', 'timezone'] from df in-place.

Assignment Part-08: Analyze Temporal Data
Question: How would you check the minimum and maximum values in the datetime column?

Assignment Part-09: Filter Columns by Correlation
Question: How do you select only following given environment-related columns and price from 'df' dataframe?

enviroment_cols = ['temperature', 'apparentTemperature',
'precipIntensity', 'precipProbability', 'humidity', 'windSpeed',
'windGust', 'windGustTime', 'visibility', 'temperatureHigh',
'temperatureHighTime', 'temperatureLow', 'temperatureLowTime',
'apparentTemperatureHigh', 'apparentTemperatureHighTime',
'apparentTemperatureLow', 'apparentTemperatureLowTime',
'dewPoint', 'pressure', 'windBearing', 'cloudCover', 'uvIndex',
'visibility.1', 'ozone', 'sunriseTime', 'sunsetTime', 'moonPhase',
'precipIntensityMax', 'uvIndexTime', 'temperatureMin',
'temperatureMinTime', 'temperatureMax', 'temperatureMaxTime',
'apparentTemperatureMin', 'apparentTemperatureMinTime',
'apparentTemperatureMax', 'apparentTemperatureMaxTime', 'price']


Assignment Part-10: Drop Low-Correlation Features
Question: If environment columns have low correlation with price,
how would you drop all 36 environment related columns except price column?

Assignment Part-11: Handle Boolean Values in Categorical Encoded Variables
Question: Use the follwoing python code to convert given categorical columns in one-hot encoding and then
replace True / False values in 'df_prep' dataframe with 1 / 0.
df_prep = pd.get_dummies(df, columns=['icon', 'source', 'destination', 'cab_type', 'name'])

Assignment Part-12: Detect Outliers with Boxplot
Question: Generate a boxplot to visualize outliers in the price column using boxplot() function of seaborn.

Assignment Part-13: Remove Outliers Using IQR
Question: For the price column, calculate IQR and filter rows where price < Q3 + 1.5*IQR.

'''

import numpy as np
import pandas as pd

data=pd.read_csv('rideshare_dataset.csv')
df=pd.DataFrame(data)
# print(df[0:1000])
# print(data.shape)
print(data.info())

# df3=df.isnull()
# print(df3)

# df4=df['price'].dropna()
# print(df4)

# column=['id', 'latitude', 'longitude', 'product_id', 'timezone']
# df5=df[column].dropna(axis=1)
# print(df5)

min=df['datetime'].min()
max=df['datetime'].max()
print("min= ",min)
print("max=",max)


enviroment_cols = ['price','temperature', 'apparentTemperature',
'precipIntensity', 'precipProbability', 'humidity', 'windSpeed',
'windGust', 'windGustTime', 'visibility', 'temperatureHigh',
'temperatureHighTime', 'temperatureLow', 'temperatureLowTime',
'apparentTemperatureHigh', 'apparentTemperatureHighTime',
'apparentTemperatureLow', 'apparentTemperatureLowTime',
'dewPoint', 'pressure', 'windBearing', 'cloudCover', 'uvIndex',
'visibility.1', 'ozone', 'sunriseTime', 'sunsetTime', 'moonPhase',
'precipIntensityMax', 'uvIndexTime', 'temperatureMin',
'temperatureMinTime', 'temperatureMax', 'temperatureMaxTime',
'apparentTemperatureMin', 'apparentTemperatureMinTime',
'apparentTemperatureMax', 'apparentTemperatureMaxTime', 'price']

df6=df[enviroment_cols]
print(df6)