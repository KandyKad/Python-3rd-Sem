def is_palindrome(str1):
    str2 = str1[::-1]
    if(str1==str2):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome")
    
my_str = input("Enter a string: ")
is_palindrome(my_str)
