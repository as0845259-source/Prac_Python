l = [20 , 30 , 50 , 60]
del l[1] #not return
print(l)

l.pop(2)
print(l) #can return

r = [20 , 30 , 50 , 60]
r.remove(50) #work on value
print(r)

r.clear() #clear all list
print(r)
 
l[0] = 90
print(l) #update the value in list

i = [20 , 30 , 40 , 50]
i.insert(0,10)     #Insert the value at any positon
print(i)

i.append(60)
print(i)   #append value at the end of the list not any position

a = [10 , 20 , 30 , 40 ]
p = [50 , 60]
a.append(p)
print(a)  # add list in to list >>> nested list append paste complt data type


a.extend(p)
print(a)  # pasted value only not data type