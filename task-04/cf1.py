n,m,a=map(int,input().split()) 
 
if m%a==0: 
    rad1=m//a 
else: 
    rad1=m//a+1 
 
if n%a==0: 
    rad2=n//a 
else: 
    rad2=n//a+1 
 
print(rad1*rad2) 