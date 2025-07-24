import matplotlib.pyplot as plt
import numpy as np

n=5+np.random.randn(100)

print("n = ",n)
m=list(range(len(n)))
print("m = ",m)

plt.bar(m,n)
plt.title("Raw Data")
plt.show()


plt.hist(n,bins=10)
plt.title("Histogram")
plt.show()