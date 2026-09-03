class Area:
    def find_area(self,a=None,b=None):
        if a!=None and b!=None:
            print(a*b)
        elif a!=None:
            print(a*a)
        else:
            print("Nothing")
myobject = Area()
myobject.find_area()
myobject.find_area(10)
myobject.find_area(20,20)    


class std1:
    def myFunction(self):
        print("i am in class A")
class std2(std1):   
    def myfunction(self):
        print("i am in class B")
        
obj = std2()
obj.myFunction()                            