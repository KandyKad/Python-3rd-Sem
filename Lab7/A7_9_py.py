'''def Count(str1):
    upper, lower, number, special = 0, 0, 0, 0
    for i in range(len(str1)):
        if str1[i] >= 'A' and str1[i] <= 'Z': 
            upper += 1
        elif str1[i] >= 'a' and str1[i] <= 'z': 
            lower += 1
        elif str1[i] >= '0' and str1[i] <= '9': 
            number += 1
        else:
            special += 1 

def password_verify(my_str):
    l = len(my_str)
    if l>=6 and l<=12:
        if upper>=1 and lower>=1 and number>=1 and special>=1:
            print(my_str)
        else:
            print() 
    else:
        print()


# Driver Code 
my_str = [input("Enter your password for the required username: ").split(",")]
for i in my_str:
    Count(i)
    print(password_verify(i))
print(my_str)
'''
'''
import re
pw = [input("Enter your password for the required username: ").split(",")]
for i in pw:
    x = 2
    print(not re.search("[a-z]",i))
    while x:
        if (len(i)<6 or len(i)>12):
            break
        elif not re.search("[a-z]",i):
            break
        elif not re.search("[0-9]",i):
            break
        elif not re.search("[A-Z]",i):
            break
        elif not re.search("[$,_,@]",i):
            break
        elif re.search("\s",p):
            break
        else:
           print(i," is a Valid Password.")
           x = 3
           break
if x==2:
    print("Not a Valid Password.")
'''
'''
list = input("Enter the list of passwords\n").split(",")
list_f = []
for i in list:
    r1,r2,r3,r4,r5,r6=0,0,0,0,0,0
    for j in i:
        if(j.islower()):
            r1+=1
        if(j.isupper()):
            r2+=1
        if(j.isdigit()):
            r3+=1
        if(j=='$' or j=='_' or j=='@'):
            r4+=1
        if(len(i)>=6 and len(i)<=12):
            r5+=1

        if(r1>0 and r2>0 and r3>0 and r4>0 and r5>0):
            list_f.append(i)
            break

print(list_f)
        
'''
print("Check your password below: ")
symbol = {'$','@','#'}
valid = []
passwordList = input("Enter list of passwords\n").split(',')
for p in passwordList:
    if(len(p) in range(6,12) and not p.isupper() and not p.islower() and not p.isdigit() and set(p).intersection(symbol)):
       valid.append(p)
print(valid)

#Test cases: Kk@123ku,As$145lk,Dl#1235k
