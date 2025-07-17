# Using -1 to infer a dimension , -1 means auto detect the dimension

import  numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,1,2,3,4,5,6,7,8,9,10,11,12])
print(arr)

# -1 allows to calculate the number of rows based on the total number of elemnets
reshape_arr=np.reshape(arr,(3,-1,2))  # inflatetion of Data
print(reshape_arr)