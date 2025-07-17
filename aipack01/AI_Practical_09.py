# Practical 09:
# Dictionary

person={
    "name":"Ambuj",
    "age":21,
    "city":"Greater Noida"
}

print("Dictonary", person)


# Modify value
person["age"]=22  # modify
person["job"]="Engineer"  # add new key pair

print(person)

print(list(person.items()))  # list of tuples

for key in person:
    print(key ,"====", person[key])

print("----------------------------------------------------------------")
for k,v in person.items():
    print(k, "====", v)

di={
    'A':[111,112,114],
    'B':[222,223,224],
    'C':[333,334,335]
}

print("di = ",list(di.items()))
for ch, arr in di.items():
    print(ch, end="\t")
    for n in arr:
        print(n,end="\t")
    print("\n")



# Practical 09:
# Dictionary

# 1️⃣ Create a dictionary
person = {
    "name": "Ambuj",
    "age": 21,
    "city": "Greater Noida"
}

print("Original Dictionary:", person)

# 2️⃣ Accessing values
print("Name:", person["name"])           # using key directly
print("City:", person.get("city"))       # using get() method

# 3️⃣ Modifying an existing value
person["age"] = 22
print("After modifying 'age':", person)

# 4️⃣ Adding a new key-value pair
person["job"] = "Engineer"
print("After adding 'job':", person)

# 5️⃣ Removing a key-value pair using pop()
person.pop("city")
print("After removing 'city':", person)

# 6️⃣ Using del to delete a key
del person["job"]
print("After deleting 'job':", person)

# 7️⃣ Using popitem() to remove the last inserted item (Python 3.7+)
last_item = person.popitem()
print("After popitem():", person)
print("Popped item:", last_item)

# 8️⃣ Checking if a key exists
print("Is 'name' in dictionary?", "name" in person)

# 9️⃣ Loop through keys and values
print("Looping through dictionary:")
for key, value in person.items():
    print(f"{key} : {value}")

# 🔟 Get all keys and values separately
print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items())

# 🔁 Copy dictionary
person_copy = person.copy()
print("Copied Dictionary:", person_copy)

# 🔄 Clear all items from dictionary
person.clear()
print("After clear():", person)
