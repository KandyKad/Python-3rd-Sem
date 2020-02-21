
#Normal method
def div_by_7():
    for i in range(0,n):
        if(i%7==0):
            yield i

n = int(input("Enter a range for the number: "))
for i in div_by_7():
    print(i, end=",")

'''
#Using try and finally functions
def div_by_7():
    try:
        for i in range(0,n-7):
            if(i%7==0):
                yield i
    finally:
        for i in range(n-7,n):
            if(i%7==0):
                yield (i)
                
n = int(input("Enter a range for the number: "))
for i in div_by_7():
    print(i, end=",")
'''
'''
#Without trailing comma
def div_by_7():
    for i in range(0,n-7):
        if(i%7==0):
            yield i        

n = int(input("Enter a range for the numbers: "))
for i in div_by_7():
    print(i, end = ",")
print(' '.join([str(elem) for elem in [i for i in range(n-7,n) if i%7==0]]))
'''
