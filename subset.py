arr=list(map(int,input().split()))
n=len(arr)
t_subset=(1<<n)
ans=[]
for num in range(t_subset):
    curr_subset=[]
    for i in range(n):
        if(num&(1<<i)!=0):
            curr_subset.append(arr[i])
    ans.append(curr_subset)
print(ans)                                  
