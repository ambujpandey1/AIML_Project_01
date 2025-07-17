#Practical-17

s1=input("Enter any word :")
s1=s1.upper()
print("Input Data =", s1)

count=0

for alpha in s1:
    if alpha=='A' or alpha=='E' or alpha=='I' or alpha=='O' or alpha=='U':
         count=count+1
print("Total vow =" ,count)
print("Total cons =",len(s1)-count)