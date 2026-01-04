# def func(x,n):        # print x n times using recursion
#     if n==0:
#         return
#     print(x)
#     func(x,n-1)
# func(1,4)

# def func(i,n):        # print i to n using head recursion
#     if i>n :
#         return
#     print(i)
#     func(i+1,n)
# func(1,4)

# def func(n):             # print i to n using tail recursion
#     if n<1 :
#         return
#     func(n-1)
#     print(n)
# func(4)

# def func(i,n):         # print n to i using tail recusion
#     if i>n :
#         return
#     func(i+1,n)
#     print(i)
# func(1,4)

# def func(n):             # print n to i using head recusion
#     if n==0 :
#         return
#     print(n)
#     func(n-1)
# func(4)

# def func(sum,x,y):        #print sum 1 to n using recursion
#     if x>y :
#         print (sum)
#         return
#     func(sum+x,x+1,y)
# func(0,1,4)

# def func(n):               #using functional recursion we add n to 1
#     if n==1 :
#         return 1
#     return n+func(n-1)
# print(func(4))

def factorial(n):
    if n==1 :
        return 1
    return n*factorial(n-1)
print(factorial(4))