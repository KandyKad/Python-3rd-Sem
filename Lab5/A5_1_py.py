import math
num = input("Enter a number").split(",")
mylist = []
for i in num:
    n = math.factorial(int(i))
    mylist.append(n)
print(tuple(mylist))
