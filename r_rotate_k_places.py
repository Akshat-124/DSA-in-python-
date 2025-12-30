# def r_rotate_k(nums,k):           #brute force
#     n=len(nums)
#     rotations=k%n
#     for _ in range(0,rotations):
#         e=nums.pop()
#         nums.insert(0,e)
#     return nums
# nums=[3,9,5,6,7,2]
# print(r_rotate_k(nums,3))

def r_rotate(nums,k):
    n=len(nums)
    k=k%n
    nums[:]=nums[n-k: ]+nums[ :n-k]
    return nums
nums=[3,9,5,6,7,2]
print(r_rotate(nums,3))

