'''
# 1st code

import collections
mylist = [1,2,3,4,5,6,2,4,1,5,3,6,2,1]
print("Original List : ", mylist)
ctr = collections.Counter(mylist)
print("Frequency of the elements in the list : ", ctr)

'''

"""
# 2nd code

mylist = [1,2,3,4,5,6,2,4,1,5,3,6,2,1]
for i in mylist:
    c = mylist.count(i)
    print("Frenquency of {} : {}".format(i,c))

"""

'''
# 3rd code

def CountFrequency(my_list):
    freq = {}
    for item in my_list :
        if(item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        print("Frequency of %d : %d"%(key,value))

if __name__ == "__main__":
    my_list = [1,2,3,4,5,6,2,4,1,5,3,6,2,1]

    CountFrequency(my_list)
'''

# 4th code

mylist = [1,2,3,4,5,6,2,4,1,5,3,6,2,1]
nlist = []
for item in mylist:
    if item not in nlist:
        nlist.append(item)
for item in nlist:
    print("Frequency of ",item," : ",mylist.count(item))

