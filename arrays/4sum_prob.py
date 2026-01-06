# def four_sum(nums,target):                   #bruteforce(TC=o(n^4),SC=o(n))  ##leetcode18##
#     n=len(nums)
#     if n<4:
#         return []
#     my_set=set()
#     for i in range(0,n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 for l in range(k+1,n):
#                     total=nums[i]+nums[j]+nums[k]+nums[l]
#                     if total == target:
#                         temp=[nums[i],nums[j],nums[k],nums[l]]
#                         temp.sort()
#                         my_set.add(tuple(temp))
#     result=[]
#     for ans in my_set:
#         result.append(list(ans))
#     return result
# nums=[1,0,-1,0,-2,2,5,9]
# print(four_sum(nums,0))

print("-----------------")

def four_sum(nums,target):                             #better sol (TC=o(n^3),SC=o(n))
    n=len(nums)
    my_set=set()
    for i in range (0,n):
        for j in range (i+1,n):
            hash_set=set()
            for k in range(j+1,n):
                fourth=target-(nums[i]+nums[j]+nums[k])
                if fourth in hash_set:
                    temp=[nums[i],nums[j],nums[k],fourth]
                    temp.sort()
                    my_set.add(tuple(temp))
                hash_set.add(nums[k])
    result=[] 
    for ans in my_set:
        result.append(ans)
    return result
nums=[1,0,-1,5,-2,2,0,9]
print(four_sum(nums,0))



