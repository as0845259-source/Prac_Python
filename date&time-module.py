import datetime

# datetime.datetime.now()
x = datetime.datetime.now()
print(x)

d = datetime.datetime(2026,9,3)
print(d)

# logics 

a = datetime.datetime.now()
m = a.strftime("%I")
print(m)