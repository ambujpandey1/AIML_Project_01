#AIpractical168

#StandardScalar
#----------------
#  Standardize data (0 mean, 1 stdev) :
#  Mean removal and variance scaling

#StandardScaler = X - mean(X) / stdev(X)

from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

filename = 'indians-diabetes.data.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
#           0       1       2       3        4      5        6      7      8

dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values

# separate array into input and output components
X = array[: , 0:8]
Y = array[: , 8]

scaler = StandardScaler()
rescaledX = scaler.fit_transform(X)

print( rescaledX[ :30 , :] )

print( "\n\nMean of First coloum=" , end="")
print(    np.mean( rescaledX[ : , 0] )     )

print( "\n\nMean of Second coloum=" , end="")
print(    np.mean( rescaledX[ : , 1] )     )