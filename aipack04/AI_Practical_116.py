import pandas as pd

restored_df=pd.read_excel('outputData.xlsx',sheet_name='GNIOT_Sheet',index_col=None,na_values=['NA'])

print(restored_df)