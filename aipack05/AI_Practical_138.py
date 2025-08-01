#Using interpolate() function to fill the missing values using linear method.
import pandas as pd
# Creating the dataframe
df = pd.DataFrame(
                    {   "A": [12,   4,   5,    None, 1   ],
                        "B": [None, 2,   54,   3,    None],
                        "C": [20,   16,  None, 3,    8   ],
                        "D": [14,   3,   None, None, 6   ]
                    }
                )

print("\n df= \n", df )    # Print the dataframe

#Let’s interpolate the missing values using Linear method.
# Note that Linear method ignore the index and treat the values as equally spaced.
# To interpolate the missing values
df2 = df.interpolate( limit_direction ='forward')
print("\n df2= \n", df2 )
#As we can see the output, values in the first row could not
# get filled as the direction  of filling
#  of values is forward and there is no previous value which
#  could have been used in interpolation.

df3 = df.interpolate( limit_direction ='backward')
print("\n df3= \n", df3 )