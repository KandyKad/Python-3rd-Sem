class subset:

    def s1(self,a1):
        return self.s2([], sorted(a1))

    def s2(self, curr, a1):
        if a1:
            return self.s2(curr, a1[1:]) + self.s2(curr+[a1[0]], a1[1:])
        return[curr]
    
    def getList(self):
        self.a = [input("Enter a list of integers:").split(" ")]
#a=subset()
n = int(input("Enter number of elements : ")) 
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
#a = list[int(input("Enter the elements of the list: ").split(" "))]
#a.getList()
print("Subsets of the list are: ")
print(subset().s1(a))
#print(a)
        
