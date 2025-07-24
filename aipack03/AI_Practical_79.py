import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(-np.pi,np.pi,255,endpoint=True)
print("X= ",x)

S=np.sin(x)
C=np.cos(x)

plt.plot(x,S,label='sine curve')
plt.plot(x,C,label='cos curve')
plt.grid(True)

plt.legend(loc="upper left")
plt.show()