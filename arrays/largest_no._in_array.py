def largest_element(nums):
    largest=nums[0]
    n=len(nums)
    for i in range (0,n):
        largest=max(largest,nums[i])
    return largest
nums=[55,90,-99,3,67]
print(largest_element(nums))