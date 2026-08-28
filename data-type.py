# NUMBER TYPE : 3 type of data INT , FLOAT , COMPLEX
a = 5
print(a,type(a))

b = 10.5
print(b,type(b))

c = 2+5j
print(c,type(c))

# STRING TYPE :     Written in singal double & tripal quotations

str1 = "This is pyton"
print(str1,type(str1))

str2 = '''HEllO!
 My Name is python'''
print(str2,type(str2))

# LIST TYPE : Value Can be Changed

list = [1 , 2.2 , 'list']
list[1] = 10.5
print(list,type(list))

# TUPLE TYPE : More Then 1 Value Working like list but more faster then list

t = (1 , 'tuple' , 2026)
print(t,type(t))

# DIRECTORY TYPE : Worked with both Key and Value 

d = {
    'courseName' : 'Pyton' ,
    'courseSize' : '2 Months'
}
print(d['courseName'])
print(d,type(d))

# SET TYPE : Not Repeat the same value

s = {10 , 20 , 30 , 40 , 50 ,10}
print(s,type(s))