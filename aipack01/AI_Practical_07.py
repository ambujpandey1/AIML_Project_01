# Practical-07

# 1️⃣ Create a List
# fruits_list = ["apple", "banana", "cherry", "apple"]
# print("1. List:", fruits_list)
# fruits_list.append("Mango")
# print(fruits_list)
# fruits_list.remove("apple")
# print(fruits_list)
# fruits_list[1]="Ambuj"
# print(fruits_list)
# Create a List
fruits_list = ["apple", "banana", "cherry", "apple"]
print("Original List:", fruits_list)

# 1️⃣ Append - Add an element to the end of the list
fruits_list.append("Mango")
print("After append('Mango'):", fruits_list)

# 2️⃣ Remove - Remove first occurrence of a specific element
fruits_list.remove("apple")
print("After remove('apple'):", fruits_list)

# 3️⃣ Update - Change value at a specific index
fruits_list[1] = "Ambuj"
print("After updating index 1 to 'Ambuj':", fruits_list)

# 4️⃣ Insert - Add element at a specific position
fruits_list.insert(2, "Orange")
print("After insert(2, 'Orange'):", fruits_list)

# 5️⃣ Pop - Remove element at a given index (default last)
fruits_list.pop()
print("After pop():", fruits_list)

# 6️⃣ Count - Count how many times an item appears
apple_count = fruits_list.count("apple")
print("Count of 'apple':", apple_count)


# 8️⃣ Sort - Sort the list in ascending order
fruits_list.sort()
print("After sort():", fruits_list)

# 9️⃣ Reverse - Reverse the list order
fruits_list.reverse()
print("After reverse():", fruits_list)

# 🔟 Length - Total number of items
print("Length of list:", len(fruits_list))
