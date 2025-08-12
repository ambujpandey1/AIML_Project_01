import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('insurance_data2.csv')
print( df.head() )

x = df.iloc[ : , 0:1].values
#           row, col
y = df.iloc[:, 1].values
print(x)
print(y)

plt.title("Insurance data")
plt.xlabel("Age")
plt.ylabel("Insured or not")
plt.scatter(x,y,color='r')
# plt.show()

n = np.size(x)
m_x = np.mean(x)
m_y = np.mean(y)

ss_xy = np.sum(x * y) - n * m_x * m_y
ss_xx = np.sum(x * x) - n * m_x * m_x

m = ss_xx / ss_xy
c = m_y - m * m_x

print("Value of m: ",m)
print("Value of c: ",c)

print("\nModel :  y=",m,"x+",c)

plt.scatter(x, y, color='r', marker='o', s=30)
y_pred = c + m * x

plt.scatter(x, y_pred, color='g', marker='o', s=60)
plt.plot(x, y_pred, color='b')

plt.xlabel("--------------X--------------->")
plt.ylabel("--------------Y--------------->")

plt.show()