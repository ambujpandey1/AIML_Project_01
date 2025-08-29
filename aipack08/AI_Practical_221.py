import warnings
warnings.filterwarnings(action="ignore")

import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.pipeline import Pipeline

# load data
filename = 'indians-diabetes.data.csv'
hnames=['preg', 'plas', 'pres', 'skin', 'test','mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

# create pipeline

arr = []
arr.append(  ("standardize" , StandardScaler() ) )
arr.append(  ("logistic" , LogisticRegression() ) )

pipelineModel = Pipeline(arr)
print("\n\n")
# evaluate pipeline
kfold = KFold(n_splits=10, shuffle=True, random_state=7)
results = cross_val_score(pipelineModel, X, Y, cv=kfold)

print("Accuracy: %.2f %% " %  (results.mean() * 100 )   )