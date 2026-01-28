def power(nums):     #TC=o(2^n *)
    n=len(nums)
    total_subset=1<<n
    result=[]
    for num in range (0,total_subset):
        lst=[]
        for i in range (0,n):
            if num & (1<<i) != 0:
                lst.append(nums[i])
        result.append(lst)
    return result
nums=[1,2,3]
print(power(nums))