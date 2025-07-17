#practical :21
import pickle
cities=["Lucknow","Noida","Delhi","Kanpur"]
students=['Jeetendra','James','Jeet','Alisha']

pickle_object=[students,cities]
fh=open("C:\\Users\\santo\\OneDrive\\Desktop\\AIMlProject-01-GNIOT\\data2.pkl","wb")
pickle.dump(pickle_object,fh)
fh.close()

print("All students and  cities data saved successfully in pickle.")


#practical :22
fh=open("C:\\Users\\santo\\OneDrive\\Desktop\\AIMlProject-01-GNIOT\\data2.pkl","rb")
import pickle

areas=pickle.load(fh)
fh.close()
print(type(areas))
print(areas)
print("List 1 Data(students): ", areas[0])
print("List 2 Data(Cities): ",areas[1])