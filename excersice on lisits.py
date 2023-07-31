lst = [1,2,-3,-4,5,8,6,-7,8]


#a
for i in lst :
    print(i, "", end = "")
print("")    
print("----------------")   
#b
total = 1
for i in lst :
    total *= i
print(total)

print("")    
print("----------------")
#c

count = 0
for i in lst :
    if i < 0 :
     count +=1
print("the number of negative products are ",count)