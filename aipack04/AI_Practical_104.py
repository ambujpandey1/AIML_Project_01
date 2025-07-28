import pandas as pd
import numpy as np
print("numpy matrix =\n\n",np.random.randn(6,4))

#DataFrame(Data,RowHeading,ColumnHeading)
np.random.seed(0)
df=pd.DataFrame(np.random.randn(6,4),
                index=pd.date_range('20190101',periods=6,freq="D"),
                columns=['A','B','C','D'])

print("\n\npandas dataframe = \n",df)

df['E']=df['A'].apply(lambda y:1 if(y>=0) else 0)
df['F']=df['B'].apply(lambda y:'pass' if(y>=0) else "fail")

print("\n\n",df)

print("\n\n",df.groupby('E').size())

print("\n\n",df.groupby('F').size())

print("df.describe() : \n",df.describe())

print("\n\ndf.describe(include=all) : \n",df.describe(include="all"))
print("\n\ndf.describe(include=object) : \n",df.describe(include="object"))