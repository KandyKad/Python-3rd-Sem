num = [x for x in input("Enter the numbers in comma separated manner: ").split(",")]
mylist = []
for i in num:
    x = int(i,2)
    print(x)
    if not x%5:
        mylist.append(i)
print(tuple(mylist))
