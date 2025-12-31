# def missing(nums):                #brute force , TC=o(n^2)
#     n=len(nums)
#     for i in  range (0,n+1):
#         if i not in nums:
#             return i 
# nums=[1,0,3,4]
# print(missing(nums))

def missing(nums):
    n=len(nums)
    return (n*(n+1))//2 - sum(nums)
nums=[0,2,3,4]
print(missing(nums))