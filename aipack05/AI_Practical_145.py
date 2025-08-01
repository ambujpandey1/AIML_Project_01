#AIPractical_145


#Handle Missing Data with SimpleImputer in AI Algorithms
#------------------------------------------------------------

#SimpleImputer is a scikit-learn class which is helpful in handling the
# missing data in the predictive model dataset.

# It replaces the NaN values with a specified placeholder.

#It is implemented by the use of the SimpleImputer() method
# which takes the following arguments :

# 1) missing_values : The missing_values placeholder which has to be imputed.
#                     By default is NaN
# 2) strategy     : The data which will replace the NaN values from the dataset.
#                     The strategy argument can take the values –
#                      (a) ‘mean'(default),    (b) ‘median’,
#                      (c) ‘most_frequent’     (d) ‘constant’.
# 3) fill_value : The constant value to be given to the NaN data
#                 using the constant strategy.








#ML code to illustrating the use of SimpleImputer class.
import numpy as np
# Importing the SimpleImputer class
from sklearn.impute import SimpleImputer
# Imputer object using the mean strategy and  missing_values type for imputation
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

data = np.array( [  [12,     np.nan,  34    ],
                    [10,     32,      np.nan],
                    [np.nan, 11,      20    ]
                 ]  )

print("Original Data : \n", data)
imputer = imputer.fit(data)  # Fitting the data to the imputer object

# Imputing the data
data2 = imputer.transform(data)
print("\n\nImputed Data : \n", data2)
#Note: The mean or median is taken along the column of the matrix