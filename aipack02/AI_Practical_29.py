import numpy as np
ar=np.ones((4,5),dtype=int) # by default float


print("\n 6`s filled array ones = ")
print(ar*6)

print("\n")
res=np.full((5,5),6,dtype=int)
print(res)