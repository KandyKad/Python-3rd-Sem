net = 0
while(True):
    print("Enter the amount to be deposited(D) of withdrawn(W):")
    print("Eg. D 200, W 100")
    print("Hit double enter for Net Balance.")

    a = input().split(" ")

    if len(a)==2:
        
        if a[0] == 'D':
            net+=int(a[1])
        elif a[0] == 'W':
            net-=int(a[1])
    else:
        break
print("Net amount in the bank account: Rs", net)

'''
print(a)
sum1,sum2 = 0,0
for i in a:
    if (a[0]=='D'):
        t1 = int(a[2:])
        sum1 = sum1+t1
    elif (a[0]=='W'):
        t2 = int(a[2:])
        sum2 = sum2+t2

print("Net amount in the bank account: ", (sum1-sum2))
print(sum1)
print(sum2)
'''

'''
    if a:
        new = a.split()
    else:
        break
        '''
