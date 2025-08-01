import numpy as np
from sklearn.impute import SimpleImputer
# Imputer object using the most_frequent strategy and  missing_values type for imputation
imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')

data = np.array( [   [12,     np.nan, 34     ],
                     [10,     20,     34     ],
                     [np.nan, 20,     30     ],
                     [10,     20,     30     ],
                     [10,     11,     np.nan ]
                 ] )


print("Original Data : \n", data)
# Fitting the data to the imputer object
imputer = imputer.fit(data)
# Imputing the data
data2 = imputer.transform(data)
print("\n\nImputed Data : \n", data2)