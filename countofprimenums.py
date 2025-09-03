n=int(input())
prime=[1]*(n+1)
for i in range(2,int(n**0.5)+1):
    if(prime[i]==1):
        for j in range(i*i,n+1,i):
            prime[j]=0
count=0
for i in range(2,n+1):
    if(prime[i]==1):
        count+=1
print(count)
