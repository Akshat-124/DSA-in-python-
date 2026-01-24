# def max_subarray(nums):          #leetcode-53                     #brute force(TC-o(n^2))
#     n=len(nums)
#     maxi=float("-inf")
#     for i in range (0,n):
#         total=0
#         for j in range(i,n):
#             total=total+nums[i]
#             maxi=max(maxi,total)
#             i+=1
#     return maxi
# nums=[-2,1,-3,4,-1,2,1,-5,4]
# print(max_subarray(nums))

def max_subarray(nums):               #optimal sol (TC-o(n))
    n=len(nums)
    maxi=float("-inf")
    total=0
    for i in range(0,n):
        total = total + nums[i]
        maxi=max(maxi,total)
        if total < 0:
            total=0
    return maxi
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))
