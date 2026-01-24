def min_roated(nums):                    #TC=o(logn),SC=o(1)
    low=0
    n=len(nums)
    high=n-1
    mini=float("inf")
    while low<=high:
        mid=(low+high)//2
        if nums[mid]<=nums[high]:
            mini=min(mini,nums[mid])
            high=mid-1
        else:
            mini=min(mini,nums[low])
            low=mid+1
    return mini
nums=[4,5,6,7,0,1,2]
print(min_roated(nums))