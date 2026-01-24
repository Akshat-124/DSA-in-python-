# def three_sum(arr):                             #bruteforce (TC=o(n^3))
#     n=len(arr)                                  #leetcode15
#     my_set=set()
#     for i in range (0,n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 if arr[i]+arr[j]+arr[k]==0:
#                     temp=[arr[i],arr[j],arr[k]]
#                     temp.sort()
#                     my_set.add(tuple(temp))
#     return [list(ans) for ans in my_set]
# arr=[-1,0,1,2,-1,-4]
# print(three_sum(arr))

# def three_sum(arr):           #better sol (TC=o(n^2),SC=o(n))
#     n=len(arr)
#     result=set()
#     for i in range(0,n):
#         myset=set()
#         for j in range(i+1,n):
#             third=-(arr[i]+arr[j])
#             if third in myset:
#                 temp=[arr[i],arr[j],third]
#                 temp.sort()
#                 result.add(tuple(temp))
#             myset.add(arr[j])
#     return[list(list (ans) for ans in result)]
# arr=[-1,0,1,2,-1,-4]
# print(three_sum(arr))

from typing import List                              #optimal sol (TC=o(nlogn)+o(n^2),SC=o(1))
class solution:
    def threesum(self,nums:List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        nums.sort()
        for i in range(n):
            if i != 0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if total<0:
                    j+=1
                elif total>0:
                    k-=1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    ans.append(temp)
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return ans
nums=[-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
obj=solution()
print(obj.threesum(nums))
                    