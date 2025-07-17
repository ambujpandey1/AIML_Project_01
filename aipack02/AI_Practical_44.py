import  numpy as np



# Create an Deep Copy
original_array=np.array([1,2,3,4,5])
print("Oroginal_array = ",original_array)
copy_array_method=original_array.copy()
print("copy_array_method = ",copy_array_method)

copy_array_function=np.copy(original_array);
print("copy_array_function = ",copy_array_function)