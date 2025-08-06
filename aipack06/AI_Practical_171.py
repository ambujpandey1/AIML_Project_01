#AIPractical_171


# Normalize data
from sklearn.preprocessing import Normalizer
import pandas as pd

filename = 'indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test','mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=names)
array = dataframe.values
# separate array into input and output components
X = array[:, 0:8]
Y = array[:, 8]
scaler = Normalizer()
normalizedX = scaler.fit_transform(X)
# summarize transformed data

print(normalizedX[0:30, :])