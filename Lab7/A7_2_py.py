def reverse_string(str1):
    str2 = str1[::-1]

    yield str2

str1 = input("Enter a string: ")
x = reverse_string(str1)
print(next(x))







'''
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

for i in infinite_sequence():
    print(i, end=" ")
'''
