#mylist = [1,2,4,2,3,5,1,1,4,5,6,2,5,6,2,3,1,4,5]
mylist = input("Enter list elements: ").split(" ")
unique_list = []
for i in mylist:
    if i not in unique_list:
        unique_list.append(i)


print(unique_list)
