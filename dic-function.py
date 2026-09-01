d = {
    'name' : 'python',
    'fee' : 8000,
    'Duration' : '2 month'
}
n = d.get('name')
print(n)

for a in d.keys():
    print(a)

for a in d.values():
    print(a)

for a in d.items():
    print(a) 
    
del(d['Duration'])
print(d) 


n = d.pop('name')
print(d)


d = dict(name = 'python' , fee = '8000' , duration = '2 month')   
print(d)   


d.update({'fee': 10000})
print(d)


d['desc'] = 'this is python cousre'
print(d)

d.clear()
print(d)