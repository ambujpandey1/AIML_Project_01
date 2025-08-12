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
plt.scatter(x,y_dash ,color='m')
plt.plot(x,y_dash,color='r')
plt.title("Linear Regression")
plt.xlabel("Engine Temperature")
plt.ylabel("Engine Pressure")
# plt.show()



from sklearn.preprocessing import PolynomialFeatures
poly=PolynomialFeatures(degree=6)
x_poly=poly.fit_transform(x)
print('x =\n',x)
print("x_poly = \n",x_poly)

lin2=LinearRegression()
lin2.fit(x_poly,y)

plt.scatter(x,y,color='b')
y_pred=lin2.predict(x_poly)
plt.scatter(x,y_pred ,color='m')
plt.plot(x,y_pred,color='r')
plt.title("Polynomial Regression")
plt.xlabel("Engine Temperature")
plt.ylabel("Engine Pressure")
plt.legend()
# plt.show()


print("LinearRegression : ",lin.predict([[110]]))
print("PolynomialRegression : ",lin2.predict(poly.fit_transform([[110]])))
plt.scatter([110],lin.predict([[110]]) ,color='g',label='Linear Prediction')
plt.scatter([110],lin2.predict(poly.fit_transform([[110]])) ,color='y', label='Polynomial Prediction')
plt.legend()
plt.show()