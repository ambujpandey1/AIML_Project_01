import numpy as np
ddarr=np.array([[1,2,3],[4,5,6]])

print(ddarr)
print("ddarr.ndim = ",ddarr.ndim)
print("ddarr.shape = ",ddarr.shape)
print("ddarr.size = ",ddarr.size)
print("len(ddarr) = ",len(ddarr))
print("ddarr.dtype = ",ddarr.dtype)

print("ddarr[0,1] = ",ddarr[0,1])
print("ddarr[0 ] = ",ddarr[0 ])
print("ddarr[:,0] = ",ddarr[:,0])
print("ddarr[1,:] = ",ddarr[1,:])