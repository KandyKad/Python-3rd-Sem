class input_output():
    def __init__(self):
        self.str1 = ""

    def getString(self):
        self.str1 = input("Input a string: ")
        
#Dont declare with parentheses, as str object wont be callable
    def putString(self):
        print("The string is:",self.str1) 

    def putUpperString(self):
        print("The string in upper case is:",self.str1.upper())

str1 = input_output()
str1.getString()
str1.putString()
str1.putUpperString()
