# Simple Function

def myFunction():
    print('i love python')
    
myFunction()    

# Arguments Function

def newFunction(a,b=1):
    print(a+b)

n = int(input("Enter the Value 1 :"))
m = int(input("Enter the Value 2 :"))
newFunction(n,m)    

# Return Function

def returnFunction(x,y):
    a = x+y
    return a

b = returnFunction(100,100)
print(b)

    
    