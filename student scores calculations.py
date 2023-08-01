lst = [80,70,65,43,98]
def avg(t):
    sum = 0
    num = len(t)
    avreage = 0
    for i in t :
        
        sum += i
        avreage = sum / num
    return avreage
    
print(avg(lst))    
     
        
