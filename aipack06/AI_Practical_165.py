import warnings
warnings.filterwarnings(action="ignore")

import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
# import pandas.plotting as st


pd.set_option('display.width',1000)
pd.set_option('display.max_column',None)



hnames=['preg', 'plas', 'pres',
        'skin','test','mass',
        'pedi', 'age','class']

dataframe=pd.read_csv('indians-diabetes.data.csv',names=hnames)
scatter_matrix(dataframe)
# st.scatter_matrix(dataframe)
plt.show()

