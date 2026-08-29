f = "Welcome {} to {} the VS Code".format('hello' , 20)
print(f)

f = "Welcome {0} to {1} the VS Code".format(30  , 20)  # 0 store 30 & 1 store 20
print(f)

f = "Welcome {a} to {b} the VS Code".format(a=50  , b=50)  # a store 50 & b store 50
print(f)

f = "Welcome {a:^10} to {b:^10} the VS Code".format(a=50  , b=50)  # : is used for cover the space and 10 how much space
print(f)
 
# ^ = ----50----
# < = 50--------
# > = --------50
