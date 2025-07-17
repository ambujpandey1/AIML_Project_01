#practicle :19 handling data in pickle file

cities=["Lucknow","Noida","Delhi","Kanpur"]
fh=open("C:\\Users\\santo\\OneDrive\\Desktop\\AIMlProject-01-GNIOT\\data.pkl","wb")

import pickle

pickle.dump(cities,fh)
fh.close()

print("All cities data saved successfully in pickle.")
