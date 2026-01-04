# def two_d_matix(nums):        #print 2d matrix
#     rows=len(nums)
#     cols=len(nums[0])
#     for i in range (0,rows):
#         for j in range (0,cols):
#             print(nums[i][j])
#         print()
# nums=[[5,20,3],[7,-10,9],[1,-52,6]]
# print(two_d_matix(nums))

print("----------------------")

# def upr_tri(nums):                      #upr triangle
#     rows=len(nums)
#     cols=len(nums[0])
#     for i in range (0,rows):
#         for j in range (0,cols):
#             if j>=i:
#                 print(nums[i][j])
#             else:
#                 print()
# nums=[[5,20,3],[7,-10,9],[1,-52,6]]
# print(upr_tri(nums))

print("----------------------")

# def lwr_tri(nums):                       #lwr triangle
#     rows=len(nums)
#     cols=len(nums[0])
#     for i in range (0,rows):
#         for j in range (0,cols):
#             if i>=j:
#                 print(nums[i][j])
#             else:
#                 print()
# nums=[[5,20,3],[7,-10,9],[1,-52,6]]
# print(lwr_tri(nums))

print("----------------------")

def diagonal(nums):                       #diagonal'
    rows=len(nums)
    cols=len(nums[0])
    for i in range (0,rows):
        for j in range (0,cols):
            if i==j:
                print(nums[i][j])
            else:
                print()
nums=[[5,20,3],[7,-10,9],[1,-52,6]]
print(diagonal(nums))