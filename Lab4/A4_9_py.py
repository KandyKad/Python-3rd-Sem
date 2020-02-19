l1 = input("Enter a list: ").split()
x,y = input("Enter the range b/w which numbers need to be counted:").split(" ")
i=0
for b in range(int(x),int(y)):
    for c in l1:
        if b==int(c):
            i=i+1
print(i)
