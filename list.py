# Mutable
# []
# Multipal Values stored in it & list also stored in list -> nested list

l = [20 , 30 , 40 , "Python"]
print(l[1])
print(l[0] , l[1])
print(l[0:2])
print(l[1::2])

# in reverse case

print(l[-1])
print(l[-1::-2])
print(l[-1::-1])

ml = [50 , 60 , [70 , 80]]
print(ml[2][0])
print(ml[0:3])
# in reverse case
print(ml[-1])
print(ml[-1::-1])