def bigger(x,y,a):

    if x > y and x > a:
        print (x)
    elif y > x and y > a:
        print (y)
    else :
        print(a)
        
x = int(input("enter the first number"))
y = int(input("enter the second number"))
a = int(input("enter the third number"))

bigger(x,y,a)