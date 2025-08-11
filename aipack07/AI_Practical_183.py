import matplotlib.pyplot as plt
import pandas as pd
# Importing the dataset
data = pd.read_csv('LinearRegressionPoly_Data.csv')
print(data)
print(data.shape)    #(7,2)
x = data.iloc[ : , 0:1].values    # [ rows , cols ]
y = data.iloc[ : , 1].values      # [ rows , cols ]
print("X.shape = ", x.shape , "\n X=\n" , x )
print("y.shape = ", y.shape , "\n y=" , y )


from sklearn.linear_model import LinearRegression
lin=LinearRegression()
lin.fit(x,y)
y_dash=lin.predict(x)
plt.scatter(x,y,color='b')
# plt.scatter(x,y_dash ,color='m')
plt.plot(x,y_dash,color='r')
plt.title("Linear Regression")
plt.xlabel("Engine Temperature")
plt.ylabel("Engine Pressure")
plt.show()