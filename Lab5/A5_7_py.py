mylist =[]

while(True):
    print("Enter name, age, height of person in the given order:")
    print("Eg. John, 19, 91")

    a = input()
    
    if a:
        new = tuple((a.split(",")))

        mylist.append(new)
    else:
        break
mylist.sort()
print(mylist)
