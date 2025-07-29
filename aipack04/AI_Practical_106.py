import pandas as pd
import numpy as np
print("numpy matrix =\n\n",np.random.randn(6,4))

#DataFrame(Data,RowHeading,ColumnHeading)
np.random.seed(0)
df=pd.DataFrame(np.random.randn(6,4),
                index=pd.date_range('20190101',periods=6,freq="D"),
                columns=['A','B','C','D'])

print("\n\npandas dataframe = \n",df)

print("\n\nColumn wise sorting  df.sort_index(axis=1,assending=False) :\n")
print(df.sort_index(axis=1,ascending=False))



print("\n\nRow wise Sorting   df.sort_index(axis=1,assending=False) :\n")
print(df.sort_index(axis=0,ascending=False))