def my_function(w):

    counter = 0
    for k in w :
        if k == "o":
         counter += 1
        elif k == "u":
         counter += 1
        elif k == "a":
         counter += 1
        elif k == "i":
         counter += 1
        elif k == "e":
         counter += 1
        elif k == "y":
         counter +=1
       
    print("the number of vowels sounds", counter)







string = input("enter the words : ")

my_function(string)