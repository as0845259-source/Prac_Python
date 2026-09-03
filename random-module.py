import random

# random.randint()
n = random.randint(1,9) #random number between 1 , 9 & 1,9 also included
print(n)

# random.randrange()
r = random.randrange(1,9) #random number between 1 , 9 &  9 is not included
print(r)


# random.choice()
l = [10 , 20 , 30 , 40 , 50] 
c = random.choice(l)
print(c)

# random.random
r = random.random()
print(r)  #give any float value btw 0 to 1

# random.shuffle()
l = [10 , 20 , 30 , 40 , 50]
random.shuffle(l)
print(l)

# random.uniform()
u = random.uniform(1,9)
print(u) 