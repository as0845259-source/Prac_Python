str1 = "I love Python"
t = len(str1)
print(t)

for a in range(t):
    print(str1[a])
    
print() #just for space
 
# in reverse case

for a in range (t-1,-1,-1):
    print(str1[a])     
print() #just for space    
#Another method

str2 = "Welcome to the pyhton"
l = len(str2)

for a in str2 :
    print(a)
print() #just for space      
 
# in reverse case   

for a in range(l-1, -1, -1):
    print(str2[a])

    