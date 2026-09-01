l = [20 , 30 , 40 , 50 , 60 , 70]
t = len(l)
print(t)

for a in range(t):
 print(l[a])
 
# Another method

for a in l:
    print(a)
    
# in reverse case
for a in range(t-1,-1,-1):
    print(l[a])
  