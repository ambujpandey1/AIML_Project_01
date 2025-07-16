#Practical -03: fetching the training data from offline csv resource

import numpy
filename=open("C:/Users/santo/OneDrive/Desktop/AIMlProject-01-GNIOT/indians-diabetes.data.csv")
data =numpy.loadtxt(filename,delimiter=",")
filename.close()

print("Numpy loadtxt size = ",data.shape)
print("Data : \n",data)