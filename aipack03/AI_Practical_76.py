import matplotlib.pyplot as plt
from holoviews.plotting.bokeh.styles import font_size
from matplotlib.lines import lineStyles

x=[2,3,4,5,6,7]
y=[4,9,16,25,36,49]

plt.plot(x,y, marker='o',markerfacecolor='red',markersize=15,linestyle='dashed',color='blue')

plt.title("Number with Squared values",fontsize=14,color='red')
plt.xlabel('-------------Numbers----------->',fontsize=14,color='red')
plt.ylabel('-------------------Square-------------->',fontsize=14,color='blue')
plt.axis([1,8,2,51])

plt.grid(True)

plt.annotate('Square of 5',fontsize=10, color='red',xytext=(3,40),xy=(5,25),arrowprops=dict(facecolor='blue',shrink=.1))

plt.show()