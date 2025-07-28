import pandas as pd
#                        yyyy-mm-dd
dates=pd.date_range('20190101',periods=6,freq="D")

print(dates)
print("dates[0] = ",dates[0])