def read():
    print("enter date")
    month = int(input(" month: "))
    day = int(input(" day: "))
    year = int(input(" year: "))
    return (month, day, year)

date = read()
print (date)

(month, day, year) = read()
print(month,day,year)