n=input()
m=int(n)
s=0
q=m
while(m!=0):
    p=m%10
    s+=p**(len(n))
    m=m//10
if(s==q):
    print('Yes')
else:
    print('No')