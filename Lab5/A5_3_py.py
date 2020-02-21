a = input("Enter numbers in a comma separated manner: ").split(",")
mylist=[]
for i in a:
    b = ((100*int(i)/30)**(1/2))
    mylist.append(b)
print(tuple(mylist))
