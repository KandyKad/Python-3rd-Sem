num = [int(a) for a in input("Enter the numbers in comma separated fashion: ").split(",")]
mylist =[]
mylist = [mylist.append(a) for a in num]
print("List of numbers is: ", mylist)
print("Tuple of numbers is: ", tuple(mylist))
