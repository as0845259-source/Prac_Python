import pickle
file = open("writepickledata.txt","rb ")
l = pickle.load(file)
print(l)