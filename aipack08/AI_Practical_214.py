#Cross Validation Classification Report
import warnings
warnings.filterwarnings(action="ignore")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

filename = 'indians-diabetes.data.csv'
names=['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

test_data_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_data_size,random_state=seed  )
#  1       2        3       4
model = LogisticRegression()
model.fit(X_train, Y_train)   # 67% of training data
predicted = model.predict(X_test)  # 33% of test  INPUT data

report = classification_report(Y_test, predicted)

print(report)