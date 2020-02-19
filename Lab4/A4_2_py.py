l1 = [str(i) for i in input("Enter a list of words: ").split()]
n = int(input("Enter the length of words to check: "))
l2=[str(i) for i in l1 if len(i)>n]
print(l2)
