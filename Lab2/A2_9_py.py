str1=input("Enter a string : ")
str2=""
for i in range(len(str1)):
    str2+=str1[-i-1]
print("New string : ",str2)
