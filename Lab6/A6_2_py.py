a = input("Enter words: ")
mylist = a.split()
newlist = []
for i in mylist:
    if i not in newlist:
        newlist.append(i)
newlist.sort()
for i in newlist:
    print(i, ":", mylist.count(i))
