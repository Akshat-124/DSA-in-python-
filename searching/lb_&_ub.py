def lowerbound(nums,target):                  #TC=o(log(n))
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
nums=[1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
print(lowerbound(nums,7))

print("----------------------")

def upperbound(nums,target):
    n=len(nums)
    ub=n
    low=0
    high=n-1
    while low<high:
        mid=(low+high)//2
        if nums[mid]>=target:
            high=mid-1
            ub=mid
        else:
            low=mid+1
    return ub
nums=[1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
print(lowerbound(nums,7))

        