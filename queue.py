l = []
while True:
    c = int(input(''' 
                1 Push Elements
                2 pop First Element
                3 Front Elemnet
                4 Last Elemnet
                5 display queue
                6 Exit
                '''))
    if c == 1:
        i = input("Enter The Value:");
        l.append(i)
        print(l)
        
    elif c == 2:
        if len(l) == 0:
         print("Enter Value 1st then pop")
        else: 
         del l[0]
         print(l)
         
    elif c == 3:
        if len(l) == 0:
            print("Empty queue")
        else:
            print("First Element is:",l[0])    
    elif c == 4:
         if len(l) == 0:
                print("Empty queue")
         else:
            print("Last Element is:",l[-1])    
    elif c == 5:
        print ("Display queue",l)    
    elif c == 6:
        break;
    else:
        print("Invalid Opr....")
                 
        