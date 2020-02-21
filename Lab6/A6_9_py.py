mylist = [1,2,3,4,5,6,7,8,9,10]
k = list(map(lambda x:x, filter (lambda x:x%2==0, mylist)))
print(k)
