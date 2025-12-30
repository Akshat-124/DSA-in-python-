# def move(nums):                                  #bruteforce <TC=o(n)> , <SC=o(n)>
#     n=len(nums)
#     temp=[]
#     for i in range (0,n):
#         if nums[i]!=0:
#             temp.append(nums[i])
#     nz=len(temp)
#     for i in range(0,nz):
#         nums[i]=temp[i]
#     for i in range(nz,n):
#         nums[i]=0
#     return nums
# nums=[1,0,2,4,3,0,0,3,5,1]
# print(move(nums))

def move(nums):
    if len(nums)==1:
        return
    i=0
    while i<len(nums):
        if nums[i]==0:
            break
        i+=1
    if i==len(nums):
        return
    j=i+1
    while j<len(nums):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
        j+=1
    return nums
nums=[1,0,2,3,0,0,4,5]
print(move(nums))