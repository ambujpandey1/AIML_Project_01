import pandas as pd
import numpy as np
# print("numpy matrix =\n\n",np.random.randn(6,4))

#DataFrame(Data,RowHeading,ColumnHeading)
np.random.seed(0)
df=pd.DataFrame(np.random.randn(6,4),
                index=pd.date_range('20190101',periods=6,freq="D"),
                columns=['A','B','C','D'])


print("\n\npandas dataframe = \n",df)
print(df.iloc[3])

print(df.iloc[0:4,1:4])
print(df.iloc[1:4,[0,2]])

print(df.iloc[1:3,:])

print(df.iloc[:,1:3])


print("\n\n")
# both are similar but last one is more fast
print(df.iloc[1,1])
print(df.iat[1,1])
