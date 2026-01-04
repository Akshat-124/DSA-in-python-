def insertion_sort(nums):
    n=len(nums)
    for i in range(1,n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key :
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
nums=[2,5,8,5,3,9]
insertion_sort(nums)
print(nums)