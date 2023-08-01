lst = [10,20,30,90]

limit = 80

count = 0
found = False

while count < len(lst) and not found :
    if lst[count] > limit :
        found = True
    else :
        count +=1


if found :
    print ("the value is in position",count)

else :
    print ("not found")
