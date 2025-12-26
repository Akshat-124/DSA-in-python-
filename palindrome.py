# def func(s,l,r):        #recursion
#     if l>=r:
#         return True
#     if s[l]!=s[r]:
#         return False
#     return func(s,l+1,r-1)

# s="nitin"
# print(func(s,0,len(s)-1))

def func (s,l,r):
    while l<r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True
s="nitin"
print(func(s,0,len(s)-1))
