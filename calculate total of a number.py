x = int(input("enter the number"))
total = 0
while x >0 :
    dig = x % 10
    total +=dig
    x = x // 10

print(total)