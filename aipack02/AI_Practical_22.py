#Practical -22 list do not support Operation BroadCasting
list1=[1,2,3]
print("list1 * 4 = ",list1*4)
print("4 * list1 = ",4*list1)

#Practical :23
arr=(11,22,33,44,55)

for num in arr:
    print(num, " X 2 = ",num*2)

arr1=(11,22,33,44,55)
arr2=[11,22,33,44,55]
arr3=[]
for i in range(len(arr1)):
    arr3.append(arr1[i]*arr2[i])

print("arr3: ",arr3)