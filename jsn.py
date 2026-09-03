import json

d = {
    'course_name':'Python',
    'fees' : 15000
}
f = json.dumps(d)
print(f)


p ='{"cname":"python","fees":15000,"duration":"2 Month"}'
x = json.loads(p)
print(x)

# for itrations

for a in x:
    print(a,x[a])
    