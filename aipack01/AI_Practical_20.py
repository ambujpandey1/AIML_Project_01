#practical :20
fh=open("C:\\Users\\santo\\OneDrive\\Desktop\\AIMlProject-01-GNIOT\\data.pkl","rb")
import pickle

areas=pickle.load(fh)
fh.close()
print(type(areas),areas)