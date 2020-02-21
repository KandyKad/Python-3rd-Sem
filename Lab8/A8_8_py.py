class Inttoro:
    def __init__(self,num):
        self.num=num
    def convert(self):
        self.n=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
        self.sym=['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        self.i=12
        while self.num:
            self.div=self.num//self.n[self.i]
            self.num%=self.n[self.i]
            while (self.div>0):
                print("Value in Roman Numeral is:",self.sym[self.i],end="")
                self.div-=1
            self.i-=1
number=int(input("Enter an integer: "))
a=Inttoro(number)
a.convert()

