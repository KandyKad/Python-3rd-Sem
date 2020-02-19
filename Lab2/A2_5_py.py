str = input("Enter a string:")
c,d = 0,0
for i in str:
    if i.isdigit():
        c=c+1
    elif i.isalpha():
        d=d+1
print("The number of digits in string are: {}" .format(c))
print("The number of letters in string are: {}" .format(d))
