# Practical-11 :

# Example of Set and Dictionay

str = "AAABBBBCDCEEEEEABBBDDDDCCC"

set1 = set(str)
print(list(set1))

print("Presence Result : = ")
print('Z' in set1)
print('B' in set1)

freqDict = {}

for ch in set1:  # [A,B,C,D,E]
    freqDict[ch] = str.count(ch)

print(freqDict)

print("\n\n\n")
list1 = [111, 222, 333, 444, 555]
print(type(list1), list1)

t1 = tuple(list1)
print(type(t1), t1)