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

# print("\n\n",df.groupby('E').size())
#
# print("\n\n",df.groupby('F').size())

print("\n\npandas df.head() = \n")
print(df.head())
print(df.head(3))

print("\n\npandas df.tail() = \n")
print(df.tail())
print(df.tail(3))

print("\n\npandas df.sample() = \n")  // randolmy
print(df.sample())
print(df.sample(3))