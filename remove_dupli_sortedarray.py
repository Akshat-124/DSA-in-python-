# # brtute force
# def remove_duplicate(nums):
#     n=len(nums)
#     freq_map={}
#     for i in range (0,n):
#         freq_map[nums[i]]=0   #place all elements in freq map once
#     j=0
#     for k in freq_map:
#         nums[j]=k
#         j+=1
#     return j
# nums=[1,1,1,2,3,4,4,7,9,9,9,10]
# print(remove_duplicate(nums))

# optimal 
def remove_duplicate(nums):
    n=len(nums)
    i=0
    j=i+1
    if n==1:
        return 1
    while j<n:
        if nums[j] != nums[i]:
            i+=1
            nums[i],nums[j]=nums[j],nums[i]
        j+=1
    return i+1
nums=[1,1,1,2,3,4,4,7,9,9,9,10]
print(remove_duplicate(nums))