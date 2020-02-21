str = input("Enter a string: ")
count1, count2 = 0,0
for i in str:
    if (i.islower()):
        count1= count1+1
    elif (i.isupper()):
        count2 = count2+1
print("Number of upper case letters:", count2)
print("Number of lower case letters:", count1)
