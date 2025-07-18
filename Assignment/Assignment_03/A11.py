
#10 35

import numpy as np
from numpy.core.numeric import newaxis

np.random.seed(0)
temp=np.random.randint(10,36,35)
tempArr=temp.reshape(5,7)
print("Temp = ",temp)

print("\nMatrix(5 X 7) \n",tempArr)

# a) The average temperature for each city (row-wise)
avg_temp=np.mean(tempArr,axis=1)
print("\n\nAverage(Row wise sum /7):", avg_temp)


# b) The hottest day for each city (maximum temperature)
for i in range(0,5):
    print("Maximum temperature Each city +" ,i+1, "  :", np.max(tempArr[i]))

# c) The overall highest temperature recorded

print("\nOverall highest temperature : ",np.max(tempArr))



# d) Temperature deviations from the mean for each city
# print(np.std(tempArr))
std_dev=tempArr-avg_temp[:,newaxis]
print("\nTemperature deviations :\n",std_dev)

#e) Identify cities with consistent temperatures (standard deviation < 3°C)
