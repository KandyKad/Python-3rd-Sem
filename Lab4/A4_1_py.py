mylist = [int(i) for i in input("Enter the input list").split()]
num = int(input("Enter a number to check"))
l = [int(i) for i in mylist if int(i)>num]
print(l)
