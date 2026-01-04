def check_sorted_array(nums):
    n=len(nums)
    for i in range(0,n-1):
        if nums[i] > nums[i+1]:
            
            return False
    return True
nums=[1,2,3,4,5,6,5,10,16,90]
print(check_sorted_array(nums)) 