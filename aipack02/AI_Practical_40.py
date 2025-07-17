import  numpy as np

res1=np.random.rand(4)
print("\n res1 = ",res1)

np.random.seed(1)
res2=np.random.rand(4)
print("\n res1 = ",res2)

np.random.seed(0)
res3=np.random.rand(4)
print("\n res2 = ",res3)

np.random.seed(0)
res4=np.random.rand(4)
print("\n res2 = ",res4)


np.random.seed(10)
res5=np.random.rand(4)
print("\n res5 = ",res5)

#Note => Same seed number will genrates same random number

# np.random.seed(0)
res6=np.random.randint(1,20,4)
print("\n res6 = ",res6)
