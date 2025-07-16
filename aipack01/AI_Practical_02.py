#Practical -02: load csv file using python standard libaray
import csv
 #global file location (768 X 9)
filename=open("C:/Users/santo/OneDrive/Desktop/AIMlProject-01-GNIOT/indians-diabetes.data.csv")
# local file location  (768 X 9)
filename=open("C://Users//santo//OneDrive//Desktop//AIMlProject-01-GNIOT//indians-diabetes.data.csv")

reader = csv.reader(filename,delimiter=",")
lines  = list(reader)

print('No of Rows : ',len(lines) ,"\n\n")
print('List of Data : ',lines)