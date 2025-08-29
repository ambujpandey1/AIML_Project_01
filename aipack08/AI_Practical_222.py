#Example: # Create a pipeline  Feature Extraction and Modeling
#--------------------------------------------------------------
#The pipeline provides a handy tool called the FeatureUnion which
# allows the results of multiple feature selection and
# extraction procedures to be combined into a larger dataset
#  on which a model can be trained.
# Importantly, all the feature extraction and the feature union
# occurs within each fold of the cross validation procedure.

#The example below demonstrates the pipeline defined with four steps:

# 1)-Feature Extraction with Principal Component Analysis (3 features)
# 2)-Feature Extraction with Statistical Selection (6 features)
# 3)-Feature Union
# 4)-Learn a Logistic Regression Model

#The pipeline is then evaluated using 10-fold cross validation.
# Create a pipeline that extracts features from the data then creates a model

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

from sklearn.decomposition import PCA    #Reduce 8 cols into Best 3 col
from sklearn.feature_selection import SelectKBest  #Select best 6 col
from sklearn.pipeline import FeatureUnion
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# load data
filename = 'indians-diabetes.data.csv'
hnames=['preg', 'plas', 'pres', 'skin', 'test',
        'mass', 'pedi', 'age', 'class']
dataframe =  read_csv(filename, names=hnames)

array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
# create feature union
features = []
features.append(('pca', PCA(n_components=3)))
features.append(('select_best', SelectKBest(k=6)))

feature_union = FeatureUnion(features)
# create pipeline
estimators = []

estimators.append(('feature_union', feature_union))       #Feature Selection
estimators.append( ("standardize" , StandardScaler() ) )  #Data Transforation
estimators.append(('logistic', LogisticRegression()))     #Train the model
pipeedModel = Pipeline(estimators)
# evaluate pipeline
seed = 7
kfold = KFold(n_splits=10, shuffle=True ,random_state=seed)
results = cross_val_score(pipeedModel, X, Y, cv=kfold)           #Test the model for accuracy
print("Accuracy: %.2f %% " %  (results.mean() * 100 )   )