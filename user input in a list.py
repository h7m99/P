lst=[]
print("enter the values, press Q to quit : ")

user = input("")

while user.upper() != "Q" :
    lst.append(float(user))
    user = input("")

print(lst)