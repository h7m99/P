state = input ("enter M or F: ")
age = int(input("enter your age"))

if (state == "M") :
    if(24 <= age <=30) :
        print("you are accepted")
        
    else :
        print("Not accepted")
        
else :
    print("!!!!!!!")