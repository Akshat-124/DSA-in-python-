# def mark_inf(matrix,row,col):                #bruteforce (TC=o(n*m)+o(n+m)+o(n*m))
#     r=len(matrix)                             #leetcode=73#
#     c=len(matrix[0])
#     for i in range(0,r):
#         if matrix[i][col]!=0:
#             matrix[i][col]=float("inf")
#     for j in range(0,c):
#         if matrix [row][j]!=0:
#             matrix [row][j]=float("inf")
# def set_zeros(self,matrix):
#     r=len(matrix)
#     c=len(matrix[0])
#     for i in range(0,r):
#         for j in range(0,c):
#             if matrix [i][j]==0:
#                 self.mark_inf(matrix,i,j)
#     for i in range (0,r):
#         for j in range(0,c):
#             if matrix [i][j]==float("inf"):
#                 matrix[i][j]=0
    
# matrix=[[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]
# mark_inf(matrix,1,2)
# print(matrix)

def mark_zero(matrix):                        #optimal (TC=o(n*m))
    r=len(matrix)
    c=len(matrix[0])
    rowtrack=[0 for _ in range (r)]
    coltrack=[0 for _ in range (c)]
    for i in range(0,r):
        for j in range(0,c):
            if matrix [i][j]==0:
                rowtrack[i]=-1
                coltrack[j]=-1
    for i in range(0,r):
        for j in range(0,c):
            if rowtrack[i]==-1 or coltrack[j]==-1:
                matrix[i][j]=0
matrix=[[7,9,2,3],[20,8,0,10],[29,0,-10,5],[4,14,6,7]]
mark_zero(matrix)
print(matrix)