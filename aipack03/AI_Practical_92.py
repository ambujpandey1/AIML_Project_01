import numpy as np
import matplotlib.pyplot as plt


fig=plt.figure()
ax=plt.axes(projection="3d")

z=np.linspace(0,1,100)
x=z*np.sin(z*25)
y=z*np.cos(z*25)

ax.scatter3D(x,y,z,"red")
ax.set_title("3D line plot")
plt.show()
