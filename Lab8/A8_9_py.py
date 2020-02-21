class Rotoint:
    def __init__(self,s):
        self.s=s
    def convert(self):
        rom={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        val=0
        for i in range(len(self.s)):
            if i>0 and rom[self.s[i]]>rom[self.s[i-1]]:
                val+=rom[self.s[i]]-2*rom[self.s[i-1]]
            else:
                val+=rom[self.s[i]]
        print("Value in integer is:",val)
mystring=input("Enter a roman numeral: ")
a=Rotoint(mystring)
a.convert()
