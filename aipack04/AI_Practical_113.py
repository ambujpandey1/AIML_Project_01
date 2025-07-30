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
print(df.mean())

print("\nndf.B.mean() = ",df.B.mean())
print("\ndf['A'].mean() =",df['A'].mean())
print("\ndf['B'].mean() =",df['B'].mean())
print("\ndf['C'].mean() =",df['C'].mean())
print("\ndf['D'].mean() =",df['D'].mean())


print(df.mean(axis=1))  # row wise