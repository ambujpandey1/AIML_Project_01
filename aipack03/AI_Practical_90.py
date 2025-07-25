import  numpy as np
import matplotlib.pyplot as plt
from jmespath.ast import projection

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
x=[1,2,3,4,5,6,7,8,9,10]
y=np.random.randint(0,10,10)
z=np.zeros(10)

dx=np.ones(10)
dy=np.ones(10)
dz=[1,2,3,4,5,6,7,8,9,10]

ax.bar3d(x,y,z,dx,dy,dz,color='b')


ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.title("3D Bar Chart Example")
plt.legend()
plt.tight_layout()
plt.show()