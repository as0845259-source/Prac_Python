l1 = [10 , 20 , 30 , 40 ]
l2 = [60 , 70 , 80 , 90 ]
t= len(l1)
print(t)
for a,b in zip(l1,l2): # by using zip function
    print(a,b)
    
for h in range(t): #by own logic
    print(l1[h],l2[h])     
    
# when value of more then 1 list is equal then zip is work!    