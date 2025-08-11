#Practical Implementatin of LinearRegression using sklearn
#-----------------------------------------------------
import warnings
warnings.filterwarnings(action="ignore")

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def get_training_data(filename):
    dataframe = pd.read_csv(filename)
    print( dataframe )
    x_parameters = [ ]
    y_parameters = [ ]

    for  single_sqare_feet, single_price  in zip(  dataframe['square_feet'] , dataframe['price'] ):
        x_parameters.append( [single_sqare_feet]  )
        y_parameters.append(    single_price      )

    #Once we got the data, return it to main program
    return x_parameters, y_parameters

def train_linear_model(x_parameters , y_parameters, quest_value ):
    #create  Linear Regression Object
    regr = LinearRegression()
    regr.fit(x_parameters, y_parameters)    #   m & c   # Algo has been trained by fit()
    predicted_ans = regr.predict( [[quest_value]]  )  # quest_value--->700
    print("Output from machine = ", predicted_ans)

    print("After Training via sklearn: Model Parameters")
    print("m = ", regr.coef_ )   #m
    print("c = ", regr.intercept_ )  #c
    print("sklearn generated Model :   y  = ", regr.coef_, " *  x  + ", regr.intercept_)
    plt.scatter(x_parameters , y_parameters,    color="m", marker="o")
    all_predicted_Y = regr.predict( x_parameters  )
    plt.scatter(x_parameters , all_predicted_Y, color="b", marker="o")
    plt.plot(x_parameters , all_predicted_Y, color="g")
    plt.scatter(quest_value, predicted_ans, color="r")
    plt.show()

def startAIAlgorithm():
    #Collect the trainig data form external csv data file.
    x , y = get_training_data('LR_House_price.csv')
    print("Formatted Training Data : " )
    print("x = ", x )
    print("y = ", y )
    question_value = 700    #This is the question
    train_linear_model(x , y, question_value )

if __name__  ==   "__main__" :
    startAIAlgorithm()
















#Drawback of this ML Algorithm
#    1) Historic Data & ML Logic in same code file.
#    2) All Calculations done mannually
#    3) Model not applied for future predictions








'''

data[:, 0]  =======> [ 1, 2, 5, 7 ]
data[:, 0:1]=======> [ [1], [3], [5], [7]  ]

X = [ [700] ]


X = [ [1], [3], [5], [7]  ]
x =  [[150], [200], [250], [300], [350], [400], [600]]   -Univariate Linear Regression

X = [ [1,2], [3,4], [5,6], [7,8]  ]                      -Multivariate Linear Regression

X = [ [1,2,3,],[4,5,6,],[7,8,9],[10,11,12]]

X = [ [6,148,72,5],[1,85,66,29], [8,183,64,0],[1,89,66,23] ]

X = [
      [6,148,72,35,0,33.6,0.627,50],
      [1,85,66,29,0,26.6,0.351,31],
      [8,183,64,0,0,23.3,0.672,32],
      [1,89,66,23,94,28.1,0.167,21]
]
'''
















'''

import warnings
warnings.filterwarnings(action="ignore")

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Funection to gt data
def get_data(file_name):
    dataframe = pd.read_csv(file_name)
    print( dataframe )
    x_parameters = []
    y_parameters = []
    for single_square_feet, single_price_value in zip( dataframe['square_feet'], dataframe['price'] ):
        x_parameters.append( [ single_square_feet] )
        y_parameters.append(  single_price_value  )
    return x_parameters,y_parameters

# Function for Fitting data to Linear model
def linear_model_main(X_parameters, Y_parameters, quest_value):
    # Create linear regression object
    regr =  LinearRegression()  #Create an object or instance of a class
    print( "AREA : " , X_parameters  )
    print( "PRICE: " , Y_parameters  )
    regr.fit( X_parameters, Y_parameters)       # m and c for y = mx + c   We are training the algorithm
    predicted_ans = regr.predict([ [quest_value] ])    #<--quest_value=700
    predictions = {}
    predictions['coefficient'] = regr.coef_      #  m or slope or regr.coef_
    predictions['intercept']   = regr.intercept_
    predictions['predicted_ans'] = predicted_ans

    print( "Output from Machine = " , predicted_ans  )
    plt.scatter(X_parameters, Y_parameters, color="m", marker="o", s=30)

    all_predicted_Y = regr.predict(X_parameters)
    plt.scatter(X_parameters, all_predicted_Y, color="b")

    plt.plot(X_parameters, all_predicted_Y, color="r")
    plt.scatter(quest_value, predicted_ans, color="g")
    plt.show()
    return predictions

#predicting house price for house of 700 square feet area
def startAIAlogrithm():
    x, y = get_data('LR_House_price.csv')
    question_value = 700  # This is the question
    result = linear_model_main(x,y,question_value)

    print( "coefficient m=" , result['coefficient']  )
    print( "Intercept value c=" , result['intercept']  )

    print( "Predicted House Price value: ", result['predicted_ans']  )

if _name_ == "_main_":
    startAIAlogrithm()




'''