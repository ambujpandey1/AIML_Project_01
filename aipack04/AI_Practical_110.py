import pandas as pd
import numpy as np
# print("numpy matrix =\n\n",np.random.randn(6,4))

#DataFrame(Data,RowHeading,ColumnHeading)
np.random.seed(0)
df=pd.DataFrame(np.random.randn(6,4),
                index=pd.date_range('20190101',periods=6,freq="D"),
                columns=['A','B','C','D'])

print("\n\npandas dataframe = \n",df)

print("\n\n ",df.loc['2019-01-01'])

dates=pd.date_range('20190101',periods=6,freq="D")
print("\n\n",df.loc[dates[0]])



print(df.loc[:,['A','D']])

print(df.loc['20190101':'20190104',['A','D']])


# Both are similar (loc,at)
print("\n\n",df.loc[dates[0],'A'])
print(df.at[dates[0],'A'])