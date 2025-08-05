'''
#  Prepare the Data For AI/ML Algorithm
#*************************************************

# 4 Ways to Prepare the Data For AI/ML Algorithm
#-------------------------------------------------
#   1. Rescale data.   (custom range of MinMaxScaler)
#   2. Standardize data.
#   3. Normalize data.  ( 0 to 1)  Works row-wise
#   4. Binarize data.
'''

#Steps of Data Transformations
#------------------------
#Step-1: Load the dataset from a URL.

#Step-2: Split the dataset into the input and
#        output variables for machine learning.

#Step-3: Apply a pre-processing transformation
#        technique to transform only the input variables.

#Step-4: Summarize the data to show the change.
#1. Rescale Data
#----------------------
#Rescaling of Data means Transforms features by scaling each feature
#  to a given range.
#This estimator scales and translates each feature individually such that
# it is in the given range on the training set, i.e. between zero and one.

#The transformation is given by:

#X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))

#X_scaled = X_std * (max - min) + min
#1) Rescale data (custome range between 1 and 10)


import pandas as pd
from sklearn.preprocessing import MinMaxScaler

filename = 'indians-diabetes.data.csv'
hnames=['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
#         0       1       2       3        4      5        6      7      8
dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values
# separate array into input and output components
X = array[ : , 0:8]   # [ row , cols ]
Y = array[ : , 8]
scaler = MinMaxScaler( feature_range=(1,10) )   #Range

#First Method
rescaledX = scaler.fit_transform(X)

#Second Method
scaler = scaler.fit(X)
rescaledX = scaler.transform(X)

# summarize transformed data
print( rescaledX [ 0:30 , : ]   )  # [ row , cols ]


#Step-1
#  X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
#In Simple way,
#  X_std = X - min(X) / max(X) - min(X)

#Step-2
#  X_scaled = X_std * (max - min) + min


