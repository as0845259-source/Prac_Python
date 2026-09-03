import json

file = open("post.json","r")
x = file.read()
finalData = json.loads(x)
 
for a in finalData:
    print(a['title'])