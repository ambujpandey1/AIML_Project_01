#Practical -05: fetching offlline training data via Pandas

import pandas
pandas.set_option('display.max_rows' ,None)
pandas.set_option('display.max_column' ,4)

filename="C:/Users/santo/OneDrive/Desktop/AIMlProject-01-GNIOT/indians-diabetes.data.csv"
#column heading name
chnames=['preg','plas','pres','skin','test','mass','pedi','age','class']

df=pandas.read_csv(filename,names=chnames )

print("Size of training data =",df.shape)
print("\n\n",df.dtypes)
print("\n\n",df.columns)
print("\n\n",df)