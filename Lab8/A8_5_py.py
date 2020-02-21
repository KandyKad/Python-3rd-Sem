class div_by_7():

    def __init__(self,n):
        self.n = n
        
    def divby7(self):
        for i in range(self.n):
            if(i%7==0):
                yield i

n = div_by_7(int(input("Enter a range of the numbers: ")))
for i in n.divby7():
    print(i,end=",")

"""
class div:

    def __init__(self, n):
        self.n = n
        self.a = 7

    def __iter__(self):
        return self

    def __next__(self):
        i = self.a
        if(self.a>self.n):
            raise StopIteration

        self.a = self.a + 7

        return i

a = div(100)
for i in div(100):
    print(i)   
"""
