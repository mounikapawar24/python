from collections import Counter
def majorityelement(nums):
    d=Counter(nums)
    n=len(nums)
    result=[]
    for key,value in d.items():
        if(value>(n//3)):
            result.append(key)
    return result
nums=list(map(int,input().split()))
print(majorityelement(nums))
