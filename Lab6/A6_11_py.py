def fibo(n):
    if (n==0 or n == 1):
        return n
    else:
        return(fibo(n-1)+fibo(n-2))
n = int(input("Enter a number to find Nth fibonacci number: "))
print(fibo(n))
