inputok = False

while inputok == False :
    try:
        num = input("enter the number")
        num = float(num)
        
        inputok = True #all char are part of number
        
    except ValueError: #cant convert to number
        print("non numeric type entered '%s' "%num)
        
num = num*2
print(num)
        