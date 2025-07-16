import numpy as np

n4=np.array([10,-1,0,90,300,3,-6,2])

print("Before : n4 = ",n4)
n5=sorted(n4,reverse=True)   # external sorting
print("n5 : ",n5)

print("After : n4 = ",n4)

n4.sort()           # internal sorting
print("After n4.sort() = ",n4)
print("After n4.sort() = ",list(reversed(n4)))
print("After n4.sort() = ",tuple(reversed(n4)))
