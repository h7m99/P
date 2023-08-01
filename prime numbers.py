print("number"  "|"  "prime state")
print("------------------")


for i in range(1,31):
    
    if i == 1:
        print(i, "|" "false")
        
    elif i == 2 or i == 3:
        print(i, "|" "true")
        
    elif i % 2 == 0:
         print(i, "|" "false")
         
    elif i % 3 == 0:
        print(i, "|" "false")
        
    else:
        print(i, "|" "true")


    
