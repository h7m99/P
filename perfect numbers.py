

for n in range (1,101):
    su=0
    for i in range(1,n):
      if(n%i==0):
         
         su=su+i
        
                       
    if su ==n :
        print(n,"It is a perfect number")
       
   
