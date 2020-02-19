sum=0
n=int(input("Enter the no. of integers for sum and average: "))

for i in range(0,n):
    a=int(input("Enter the integer {}: ".format(i+1)))
    sum+=a
avg=sum/n
print("Sum : ", sum)
print("Average : ",avg)
