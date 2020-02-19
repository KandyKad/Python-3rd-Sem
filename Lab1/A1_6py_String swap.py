Str1 = input("Enter first string: ")
Str2 = input("Enter second string: ")
A = Str1[0]
Str1 = Str2[0]+Str1[1::]
Str2 = A+Str2[1::]
print("{} {}". format(Str1, Str2))
