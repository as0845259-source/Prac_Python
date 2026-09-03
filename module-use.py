# 1st method
import module1
print (module1.sum(10,10))
print(module1.mul(10,10))

# 2nd method

import module1 as m
print(m.sum(20,20))
print(m.mul(20,20))

# 3rd method

from module1 import sum
print(sum(30,30))

from module1 import mul
print(mul(30,30))

# 4th method

from module1 import *
print(sum(40,40))
print(mul(40,40))