class Person:
    def __init__(self):
        self.s=""
    def name(self):
        self.s=input("Enter name:")
class Address:
    def __init__(self):
        self.a=""
    def add(self):
        self.a=input("Enter Address:")
class Contact(Person,Address):
    def __init__(self):
        Person.name(self)
        Address.add(self)
        self.line="Entered information is:-"
    def print_info(self):
        print(self.line)
        print(self.s)
        print(self.a)

do=Contact()
do.print_info()
        
    
