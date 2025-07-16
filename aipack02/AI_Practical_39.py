import numpy as np

# x=np.array([[1,2],[3,4]])
#
# print("\n",x)
#
# print("Sum :",x.sum())
# print("Column wise sum:", x.sum(axis=0))
# print("Row wise sum:", x.sum(axis=1))
# print(x[:,0].sum(),x[:,1].sum())
# print(x[0,:].sum(),x[1,:].sum())

x=np.full((5,7),7,dtype=int)
print(x)
print("Column wise sum:", x.sum(axis=0))
print("Row wise sum:", x.sum(axis=1))