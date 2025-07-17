import numpy as np

# ar1=np.random.rand(2,3)
# print("ar1 =\n",ar1)
#
# ar2=ar1.reshape(1,6)
# print("ar2 =\n",ar2)
#
# ar3=ar1.reshape(6,1)
# print("ar3 = \n",ar3)
#
# ar4=ar1.reshape(6)
# print("ar4 = \n",ar4)

ar5=np.random.randint(1,100,48)
print("ar5 =\n",ar5)
print("\n")
print("\n")

ar6=ar5.reshape(3,4,-1);
print("Ar6 =\n",ar6)