# def two_sum(nums,target):       #leetcode-1                #brute force (TC=o(n^2))
#     n=len(nums)
#     for i in range(0,n-1):
#         for j in range(i+1,n):
#             if nums[i]+nums[j]==target:
#                 return[i,j]
# nums=[5,9,1,2,4,15,6,3]
# print(two_sum(nums,13))

def two_sum(nums,target):                     # optimal sol (TC=o(n),SC=o(n))
    n=len(nums)                               # using hash_map
    hash_map={}
    for i in range (0,n):
        remaining=target-nums[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        hash_map[nums[i]]=i
nums=[5,9,1,2,4,15,6,3]
print(two_sum(nums,13))