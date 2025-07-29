import pandas as pd
import numpy as np
# print("numpy matrix =\n\n",np.random.randn(6,4))

#DataFrame(Data,RowHeading,ColumnHeading)
np.random.seed(0)
df=pd.DataFrame(np.random.randn(6,4),
                index=pd.date_range('20190101',periods=6,freq="D"),
                columns=['A','B','C','D'])


print("\n\npandas dataframe = \n",df)

print("\n\n",df.A)
print("\n\n",df.A>=0)


print("\n\n")
print(df[df.A>=0])
print("\n\n")
print(df[df.B<0])


print("\n\n")
print(df[(df.A<0 )& (df.B<0)])

print("\n\n")
print(df[df.B >df.B.mean()])


print("\n\n")
print(df['B'][df.B>df.B.mean()])


print("\n\n")
print(df['B'][df.A>0])

print("\n\n")
print(df>0)

print("\n\n")
print(df[df>0])