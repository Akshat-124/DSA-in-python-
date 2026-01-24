def freq_count(nums):
    hash_map={}
    n=len(nums)
    for i in range(0,n):
         hash_map[nums[i]]=hash_map.get(nums[i],0)+1
    return hash_map
nums=list(map(int,input("enter the series of nu.: ").split(",")))
result=freq_count(nums)
print(result)