import numpy as np
print("Result-1: ",np.all([1,2,3,-4]))   #True
print("Result -2: ",np.all([1,2,3,-4,0]))   #False
print("Result-3: ",np.any([1,2,3,4]))      #True
print("Result-4: ",np.any([1,2,3,4,0]))     #True
print("Result-5: ",np.any([0,0,0.,0]))       #False
print("Result-6: ",np.any([0,0,0,0,0.,-1]))   #True