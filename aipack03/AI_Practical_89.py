import  numpy as np
import matplotlib.pyplot as plt
from jmespath.ast import projection

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
x1=[1,2,3,4,5,6,7,8,9,10]
y1=np.random.randint(0,10,10)
z1=np.random.randint(0,10,10)

x2=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
y2=np.random.randint(-10,0,10)
z2=np.random.randint(0,10,10)

ax.scatter(x1,y1,z1,c='b',marker='o',label='blue')
ax.scatter(x2,y2,z2,c='r',marker='D',label='red')


ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.title("3D Scatter plot Example")
plt.legend()
plt.tight_layout()
plt.show()