n = input("enter the cvv number ? ")
length = len(n)
if n[0:4].isdigit() and length == 8:
    print("valid cvv number")
    
else:
    print("not a valid cvv number")