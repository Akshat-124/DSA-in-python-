# def longest_seq(nums):                   #brute force (TC=o(n^2), SC=o(1))     #LeetCode=128#
#     n=len(nums)
#     max_count=0
#     for i in range (0,n):
#         num=nums[i]
#         count=1
#         while num+1 in nums:
#             count+=1
#             num = num+1
#         max_count=max(max_count,count)
#     return max_count
# nums=[1,99,101,98,2,3,5,100]
# print(longest_seq(nums))

# def longest_seq(nums):                     #better sol (TC=o(n+nlogn))  
#     n=len(nums)
#     nums.sort()
#     count=0
#     last_smaller=float("-inf")
#     longest=0
#     for i in range(0,n):
#         num=nums[i]
#         if num-1 == last_smaller:
#             count+=1
#             last_smaller=num
#         elif num != last_smaller:
#             count = 1
#             last_smaller=num
#         longest=max(longest,count)
#     return longest
# nums=[1,99,101,98,2,3,5,100]
# print(longest_seq(nums))

def longest_seq(nums):                        #optimal sol (TC=o(3n),SC=o(n))            
    n=len(nums)
    my_set=set()
    for i in range(0,n):
        my_set.add(nums[i])
        longest=0
    for num in my_set:
        if num-1 not in my_set:
            x=num
            count=1
            while x+1 in my_set:
                count+=1
                x+=1
            longest=max(longest,count)
    return longest
nums=[1,99,101,98,2,3,5,100]
print(longest_seq(nums))