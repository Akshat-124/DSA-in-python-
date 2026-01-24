def search_position(nums,target):                  #TC=o(log(n))
    n=len(nums)
    lb=n
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            high=mid-1
            lb=mid
        else:
            low=mid+1
    return lb
nums=[1,3,4,5,8,9,14,15,19,20,21]                  #returns index in which target is going to insert
print(search_position(nums,16))