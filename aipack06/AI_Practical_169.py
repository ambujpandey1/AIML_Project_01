#AIPractical_169

#StandardScalar
#----------------
#The values for each attribute in the output is now
# have a mean value of 0 and a standard deviation of 1.

import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.style.use('ggplot')
np.random.seed(1)
df = pd.DataFrame({
                    'x1': np.random.normal(0, 2, 10000),
                    'x2': np.random.normal(5, 3, 10000),
                    'x3': np.random.normal(-5, 5, 10000)
                  })
print(df)

scaler = preprocessing.StandardScaler()
scaled_df = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_df, columns=['x1', 'x2', 'x3'])

fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(6, 5))

ax1.set_title('Before Scaling')
sns.kdeplot(df['x1'], ax=ax1)
sns.kdeplot(df['x2'], ax=ax1)
sns.kdeplot(df['x3'], ax=ax1)

ax2.set_title('After Standard Scaler')
sns.kdeplot(scaled_df['x1'], ax=ax2)
sns.kdeplot(scaled_df['x2'], ax=ax2)
sns.kdeplot(scaled_df['x3'], ax=ax2)
plt.show()

#Parameters of np.random.normal() function:
# 1) loc:(float, optional)
#    The mean (center) of the normal distribution. Default is 0.0.

# 2) scale:(float, optional)
#    The standard deviation (spread or width) of the normal distribution. Default is 1.0.

# 3) size:(int or tuple of ints, optional)
#    The shape of the output array. If None, a single value is returned.


'''
Skewed ,kertosis ?
'''