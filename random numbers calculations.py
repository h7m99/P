import random
ans = ""


while ans != "done" :
    
    x = (random.randint(1,100))
    y = (random.randint(1,100))
    t = str(x + y)
    print( x, "+", y)
    ans = (input("what is the answer"))
    
    if ans == t :
     print("correct")
    elif ans == "done" :
        print("see you")
   
    else:
        print("wrong answer, try again")
    
    
    

    

