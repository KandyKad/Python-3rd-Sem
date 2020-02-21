def geek(): 
    pass

def fun():
    global e
    e = 5
    a, b, c = 1, 2.25, 333
    str = 'GeeksForGeeks'
    mylist = [1,2,Python,3.4]
    mytuple = (1,2,3,4)
    myset = {2,py,3.6}
    mydict = {1:4,2:5,3:6}
  
# Driver program 
print(geek.__code__.co_nlocals) 
print(fun.__code__.co_nlocals) 

'''
def fun(): 
    a = 1
    str = 'GeeksForGeeks'
    
# Driver program 
print(fun.__code__.co_nlocals)'''
