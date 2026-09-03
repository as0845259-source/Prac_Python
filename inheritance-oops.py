# Singal Inheritance
class A:
    def myFunction(self):
        print("I Love Python A")
        
class B(A):
    def myFunction1(self):
        print("I Love Python B")
myObject =B()
myObject.myFunction()
myObject.myFunction1()

# Multiline Inheritance

class C:
    def myFunction2(self):
        print("I Love Python C") 
class D(C):
    def myFunction3(self):
        print("I Love Python D")
class E(D):
    def myFunction4(self):
        print("I Love Python E")

myobj = E()
myobj.myFunction2()
myobj.myFunction3()
myobj.myFunction4() 

# Multipal Inheritance

class F:
    def myFunction5(self):
        print("I Love Python F")
class G:
    def myFunction6(self):
        print("I Love Python G")
class H(F,G):
    def myFunction7(self):
        print("I Love Python H") 
        
object = H()
object.myFunction5()
object.myFunction6()
object.myFunction7()                                                                                   