Str = input("Enter a string: ")
a = len(Str)
b = Str[-3:]
if a>2:
    if b == 'ing':
        print(Str+'ly')
    else:
        print(Str+'ing')
else:
    print(Str)

