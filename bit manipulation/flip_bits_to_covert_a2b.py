def flip(start,goal):
    ans=start^goal                     #TC=0(32),SC=o(1)
    count=0
    for i in range (0,32):
        if ans&(1<<i)!=0:
            count+=1
    return count
print(flip(3,4))    #counts no. of 1s i.e 3 and its our ans