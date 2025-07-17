# Practical 08 tuple

colors=("red","green","blue","red")
print(colors)
print("First color : ",colors[0])

# try to modify (will fail)

try:
    colors[1]="yellow"
except TypeError:
    print("Tuples are immutable! can not  nodify.",TypeError)



# Practical 08 - Tuple

colors = ("red", "green", "blue", "red")
print("Tuple:", colors)

# 1️⃣ Accessing Elements
print("First color:", colors[0])
print("Last color:", colors[-1])

# 2️⃣ Count - How many times an element appears
print("Count of 'red':", colors.count("red"))

# 3️⃣ Index - Position of first occurrence
print("Index of 'green':", colors.index("green"))

# 4️⃣ Slicing - Accessing a range of elements
print("Sliced tuple (1 to 3):", colors[1:3])

# 5️⃣ Length - Total number of items
print("Length of tuple:", len(colors))

# 6️⃣ Membership Test - Check if value exists
print("Is 'blue' in tuple?", "blue" in colors)

# 7️⃣ Iteration - Loop through tuple
print("Iterating over tuple:")
for color in colors:
    print(color)

# 8️⃣ Concatenation - Combine tuples
extra_colors = ("yellow", "black")
combined = colors + extra_colors
print("Combined Tuple:", combined)

# 9️⃣ Repetition - Repeat tuple
repeated = colors * 2
print("Repeated Tuple:", repeated)

# 🔟 Immutability Test - Try to modify (will fail)
try:
    colors[1] = "yellow"
except TypeError:
    print("Tuples are immutable! Cannot modify elements.")
