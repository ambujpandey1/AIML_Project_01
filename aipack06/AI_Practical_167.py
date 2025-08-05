#StandardScalar
#----------------
#  Standardize data (0 mean, 1 stdev) :
#  Mean removal and variance scaling

# zero mean and unit variance.

#StandardScaler
#--------------------
# X - mean(X) / stdev(X)

import numpy as np
from sklearn.preprocessing import StandardScaler
data = [[0, 0],
        [0, 0],
        [1, 1],
        [1, 1]]
a = np.array(data)

print("Original Data =\n", a)

scaler = StandardScaler()
print(scaler.fit(a))

print("scaler.mean_ = ", scaler.mean_ )
data2 = scaler.transform(a)
print("After transformation \n" ,data2)

print("Mean = \n", np.mean(data2, axis=0)  )

print("Std = \n",  np.std(data2,  axis=0)  )