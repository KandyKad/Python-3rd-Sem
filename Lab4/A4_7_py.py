l1=input('Enter a list: ').split()
l2=[]
for x in l1:
    if x not in l2:
        l2.append(x)
print(l2)
