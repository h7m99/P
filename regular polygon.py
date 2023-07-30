def area(n,side):
    import math

    area = (n*(side**2)) / (4* ((math.tan((math.pi)/(n)))))
    return area

num1= int(input("enter the number of sides : "))

num2 = float( input("enter the side : "))

total = area(num1,num2)
print(total)

