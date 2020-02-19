mylist=[10,20,30,40]
s = input("Enter a string to input at the beginning of each item :")
print("Given list : ", mylist)
for i in range(len(mylist)):
    mylist[i]=s+str(mylist[i])
print("New list : ",mylist)
