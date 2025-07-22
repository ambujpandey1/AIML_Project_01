import matplotlib.pyplot as plt

x1=[1,2,3]
y1=[1,2,3]

x2=[1,2,3]
y2=[1,4,9]

plt.plot(x1,y1,'ro-',x2,y2,'bs--',linewidth=7)
plt.axis([0,4,0,10])
plt.title("Report genrated by Ambuj Pandey")

plt.show()