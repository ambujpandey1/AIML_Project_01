import pandas as pd
import numpy as np
# print("numpy matrix =\n\n",np.random.randn(6,4))

#DataFrame(Data,RowHeading,ColumnHeading)
np.random.seed(0)
df=pd.DataFrame(np.random.randn(6,4),
                index=pd.date_range('20190101',periods=6,freq="D"),
                columns=['A','B','C','D'])


print("\n\npandas dataframe = \n",df)

print("\n\n")

print("After rows deletion: \n")
print(df.drop(df.index[2:4],axis=0))  # row deletion


print("After column deletion: \n")
print(df.drop(df.columns[1:3],axis=1))