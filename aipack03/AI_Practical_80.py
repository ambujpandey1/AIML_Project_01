import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.lines import lineStyles
from  matplotlib import  pyplot as plt

plt.figure(figsize=(6,4))

x=np.linspace(-np.pi,np.pi,45,endpoint=True)
print("X= ",x)

S=np.sin(x)
C=np.cos(x)

plt.plot(x,S,color="red",linewidth=5.0,linestyle="--",label='sine curve')
plt.plot(x,C,color="blue",linewidth=7.0,linestyle="-",label='cos curve')


plt.legend(loc="upper left")
plt.xlim(-4.0,4.0)
plt.xticks(np.linspace(-4,4,9,endpoint=True))

plt.ylim(-1.0,1.0)
plt.yticks(np.linspace(-1,1,9,endpoint=True))
plt.grid(True)
plt.show()