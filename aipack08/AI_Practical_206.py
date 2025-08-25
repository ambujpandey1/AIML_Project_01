#Steps of k-Fold cross validation
#1) Split Data into 10 groups
#2) Hide one group of data(10% of data)
#3) Train the model by passing 90% of training data to fit() method of model
#4) Apply back the trained model on hiiden group of data(10% of data) to generate y'
#5) calcuate the accuracies by comparing Generted y' and y_test

#2)-Evaluate using k-Fold Cross Validation
#---------------------------------------------

import warnings
warnings.filterwarnings(action="ignore")

import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

filename = 'indians-diabetes.data.csv'

hnames = ['preg','plas','pres', 'skin','test','mass', 'pedi','age','class']
#          0       1      2       3       4     5       6      7       8
dataframe = pd.read_csv(filename, names=hnames)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
model = LogisticRegression()

num_folds = 10    # Its value is a hyperparameter
kfold = KFold(n_splits=num_folds )

results = cross_val_score(model,  X, Y, cv=kfold )

#1) Split Data into 10 groups
#2) Hide one group of data(10% of data)
#3) Train the model by passing 90% of training data to fit() method of model
#4) Apply back the trained model on hidden group of data(10% of data) to generate y'
#5) calcuate the accuracies by comparing Generted y' and y_test


print( "results : " , results  )
print(  "Accuracy: %.2f %%"  % ( results.mean()*100.0 )  )
print( "Std.Deviation= %.2f" % ( results.std()*100.0 )  )