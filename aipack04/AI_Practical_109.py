import pandas as pd
import numpy as np
# print("numpy matrix =\n\n",np.random.randn(6,4))

#DataFrame(Data,RowHeading,ColumnHeading)
np.random.seed(0)
df=pd.DataFrame(np.random.randn(6,4),
                index=pd.date_range('20190101',periods=6,freq="D"),
                columns=['A','B','C','D'])

print("\n\npandas dataframe = \n",df)

# Selcting a single column
print("\n\ndf.A = \n",df.A)
print("\n\ndf['A'] =\n",df['A'])

print("\n\ndf['D'] =\n",df['D'])


#Custome row heading
print(df['2019-01-01':'2019-01-05'])


print(df[0:3])  # index 0,1 2


print(df['20190102':'20190104'])
