def bruteforce(num):                                # method 1 with TC o(n)
    n=num
    result=[]
    for i in range (1,num+1):
        if num%i ==0:
            result.append(i)
    return result
n=int(input("enter the no.: "))
print("the no. is divisible by: ",bruteforce(n))

print("--------------------")

def bruteforce(num):                                  # method 2 with TC 0(n/2)
    n=num
    result=[]
    for i in range (1,num//2+1):                      
        if num%i ==0:
            result.append(i)
    result.append(num)
    return result
n=int(input("enter the no.: "))
print("the no. is divisible by: ",bruteforce(n))

print("--------------------")
#best method comparing TC                           
from math import sqrt                                        
def bruteforce(num):                                   # method 3 with TC o(sqrt(n))
    n=num
    result=[]
    for i in range (1,int(sqrt(num))+1):
        if num%i == 0:
            result.append(i)
            if num//i != i:
                result.append(num//i)
    return result
n=int(input("enter the no.: "))
print("the no. is divisible by: ",bruteforce(n))