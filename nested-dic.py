course = {
    'php' : {'duration' : '3 month' , 'fees' : '10000'},
    'python' : {'duration' : '2 month' , 'fees' : '15000'},
    'java' : {'duration' : '2 month' , 'fees' : '20000'}  
}
print(course)
del[course['java']['fees']]
print(course['php']['fees'])

for k,v in course.items():
    print(k,v)  #print(k,v['duration'],v['fees']) for iretation
    