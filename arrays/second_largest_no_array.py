def second_largest(nums):
    largest=float("-inf")
    s_largest=float("-inf")
    n=len(nums)
    for i in range (0,n):
        if nums[i] > largest:
            s_largest=largest
            largest=nums[i]
        elif nums[i] > s_largest and nums[i] != largest:
            s_largest = nums[i]
    return s_largest
nums=[3,7,9,23,19,65,49,76,88,6]
print(second_largest(nums))
       