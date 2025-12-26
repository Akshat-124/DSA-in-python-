def func(nums,L,R):
    arr=nums
    if L>=R :
        return
    arr[L],arr[R]=arr[R],arr[L]
    func(arr,L+1,R-1)
def reverse_array(nums,L,R):
    func(nums,1,5)
    return nums
nums = [5, 7, 6, 3, 4, 5, 8]
result = reverse_array(nums, 1, 5)
print(result)