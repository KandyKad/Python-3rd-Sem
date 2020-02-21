mylist = input("Enter list elements: ").split(" ")
def unique_list(mylist):
    u_list = []
    for i in mylist:
        if i not in u_list:
            u_list.append(i)
    return (u_list)

print (unique_list(mylist))
