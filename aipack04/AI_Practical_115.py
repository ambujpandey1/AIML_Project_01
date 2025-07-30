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
df.to_excel('outputData.xlsx',sheet_name='GNIOT_Sheet')

print("Data saved in excel file.")