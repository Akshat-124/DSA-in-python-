def binary_search(nums,target):     #iterative
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums [mid]==target:
            return mid
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
nums=[2,4,6,7,9,11,18,19]
print(binary_search(nums,6))