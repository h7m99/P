import math
def area_tri(h,b):
    area = h * (0.5*b)
    return area
def area_sqr(hight):
    area = (hight **2)
    return area

def area_cir(radios):
    area = (pi)*radios**2
    return area

def area_rec(length,width):
    area = (length * width )
    return area

def area_cil(radios, hight):
    area = (2*pi*radios)(hight + radios)
    return area 

q = int(input("choose the number of shape you want to calculate the area : "))

if q == 1 :
        
    wi = int(input("enter the width of the tringle : "))
    ba = int(input("enter the base of the tringle : "))
    print(area_tri(wi,ba))

elif q == 2 :
    
     wi = int(input("enter the hight of the square : "))
     print(area_sqr(wi))

elif q == 3 :
    wi = int(input("enter the radios of the circle"))
    print(area_cir(wi))
    
elif q == 4 :
    wi = int(input("enter the length of the rec : "))
    ba = int(input("enter the width of the rec : "))
    print(area_rec(wi,ba))

elif q == 5 :
    wi = int(input("enter the radios of the cilynder : "))
    ba = int(input("enter the hight of the cilynder : "))
    print(area_cil(wi,ba))

else :
    
    print("incurrect inputs, try again !")
    
    
    
    
        

