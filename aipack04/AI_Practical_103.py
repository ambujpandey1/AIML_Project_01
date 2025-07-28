import pandas as pd
import numpy as np
print("numpy matrix =\n\n",np.random.randn(6,4))

#DataFrame(Data,RowHeading,ColumnHeading)
df=pd.DataFrame(np.random.randn(6,4),
                index=pd.date_range('20190101',periods=6,freq="D"),
                columns=['A','B','C','D'])

print("\n\npandas dataframe = \n",df)

print("\n\nHeading in DataFrame :",df.columns)
print("\n\n Row Heading of Dataframe :",df.index)
print("\n\nValues of DataFrame: \n",df.values)