s = {10 , 20 , 30 , 40 }
print(s)
print(type(s))

for a in s:
    print(a)
    
#function in sets ..... list & tuple can be convert into sets
# sets()
a = [1, 2, 3, 4, 5]
s = set(a)
print(s)

# removed()

t = {10 , 20 , 30 , 40}
r = t.remove(30)
print(t)

# discard()

d = t.discard(40)
print(t)

# add()

a = t.add(30)
print(t)

# pop()

p = t.pop()
print(t.pop())
print(t)

# update()

l = [10 , 20 , 30 , 40 , 50]
t.update(l)
print(t) 

#  clear()

t.clear()
print(t) 
    