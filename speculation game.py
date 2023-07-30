import random
x = (random.randint(1,20))
print(x)

h = False
while not h :
    y = int(input("enter the number "))

    if y > x:
        print("go lower")
    elif y < x:
        print("go bigger")
    else :
        print ("currect!")
        h = True