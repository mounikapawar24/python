def subsets(nums):
    def generate(ind,ans,curr_subset,nums):
        if(ind==len(nums)):
            ans.append(curr_subset.copy())
            return
        curr_subset.append(nums[ind])
        generate(ind+1,ans,curr_subset,nums)
        curr_subset.pop()
        generate(ind+1,ans,curr_subset,nums)
    ind=0
    ans=[]
    curr_subset=[]
    generate(ind,ans,curr_subset,nums)
    return ans
nums= list(map(int,input().split()))
print(subsets(nums))
