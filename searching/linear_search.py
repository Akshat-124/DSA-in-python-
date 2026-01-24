def linear_search(nums,target):         #TC=o(n)
    n=len(nums)
    for i in range(0,n):
        if nums[i]==target:
            return i 
    return -1
nums=[5,4,6,7,8,3,4,100,-1]
print(linear_search(nums,100))