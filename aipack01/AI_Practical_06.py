#Practical -06: fetching online training data via Pandas
import pandas
import urllib.request

pandas.set_option('display.max_rows' ,None)
pandas.set_option('display.max_column' ,None)
hnames=['sepal-length','sepal-width','petal-length','petal-width','class',]
web_path=urllib.request.urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
dataframe=pandas.read_csv(web_path,names=hnames)

print("Shape =" ,dataframe.shape)
print(dataframe)

print("\n\n\n")
print(dataframe.values)

print("\n\n\n")
print(dataframe.columns)
print("\n\n\n")
print(dataframe.dtypes)


# to export or save the data permanently in excel

dataframe.to_excel('C:\\Users\\santo\\OneDrive\\Desktop\\AIMlProject-01-GNIOT\\IrisGniot_DataSet.xlsx',sheet_name='Sheet1',index=True)
print("All data backup exported to excel file.\n\n")


# data collection from Excel

dataframe2=pandas.read_excel('C:\\Users\\santo\\OneDrive\\Desktop\\AIMlProject-01-GNIOT\\IrisGniot_DataSet.xlsx',sheet_name='Sheet1')
print("Data from Excel =\n")

print(dataframe2)