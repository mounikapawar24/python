from collections import Counter
def majorityelement(nums):
    d=Counter(nums)
    n=len(nums)
    for key,value in d.items():
        if(value>(n//2)):
            return key
nums=list(map(int,input().split()))
print(majorityelement(nums))
