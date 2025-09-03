n=int(input())
c=0
while(n>0):
    d=n%10
    if(d%2!=0):
        c=c+1
    n=n//10
print(c)
    
