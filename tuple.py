t = (20 , 30 , 40 , 50 , 60)
l = len(t)
print(l)

for a in range(l):
 print(t[a])
 
for a in t:
    print(a)  
    
a = [10 , 20 , 30 , 40 , 50]
x =  max(a)
print(x)

n = min(a)
print(n)

c = a.count(10)
print(c)


i = a.index(40)
print(i)

s = sum(a)
print(s)

s = sum(a,10) # also 
print(s)
    