# def r_rotate(nums):              #through for loop
#     n=len(nums)
#     temp=nums[n-1]
#     for i in range (n-2,-1,-1):
#         nums[i+1]=nums[i]
#     nums[0]=temp
#     return nums
# nums=[7,5,-2,3,9,0,6,10]
# print(r_rotate(nums))    

def r_rotate(nums):
    n=len(nums)
    nums[:]=[nums[n-1]]+nums[0:n-1]
    return nums[:]
nums=[7,5,-2,3,9,0,6,10]
print(r_rotate(nums))