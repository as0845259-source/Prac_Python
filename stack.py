l = []
while True:
    c = int(input(''' 
                1 Push Elements
                2 pop Element
                3 peak Elemnet
                4 display stack
                5 Exit
                '''))
    if c == 1:
        i = input("Enter The Value:");
        l.append(i)
        print(l)
        
    elif c == 2:
        if len(l) == 0:
         print("Enter Value 1st then pop")
        else: 
         p = l.pop()
         print(p)
         print(l)
    elif c == 3:
        if len(l) == 0:
            print("Empty Stack")
        else:
            print("Peak Element is:",l[-1])    
         
    elif c == 4:
        print ("Display stack",l)
    elif c == 5:
        break;
    else:
        print("Invalid Opr....")
                 
        