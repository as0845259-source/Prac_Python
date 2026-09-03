class DemoClass:
    a = 10
    # constructor
    def __init__(self):
        print("i love Pyhton")
    
    
    def myFunction(self):  #.......Use of self
        self.c = self.a*self.a
        print(self.c)
        
    def myFunction1(self,a,b):
        print(a+b)    
         
myobj = DemoClass()
myobj.myFunction()
myobj.myFunction1(20,30)        