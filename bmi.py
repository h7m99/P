kg=float (input("enter your weight"))
h=float (input("enter your height"))
h = h/100
bmi = (kg) / (h**2)

if bmi <18.5 :
    print("underweight")
 
elif 18.5 <= bmi < 25.0 :
     print("normal")
 
elif 25.0 <= bmi < 30.0 :
     print("you are overwehigt") 
 
else  :
    print("obese")