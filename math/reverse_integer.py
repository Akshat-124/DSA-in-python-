n = int(input("enter a number: "))
num = n
while num>0 :
    last_digit = num%10
    print(last_digit)
    num=num // 10

print("--------------------")

x = int(input("enter a number: "))
num = x
count = 0
while num > 0 :
    count += 1
    num=num//10
print("no. of digits:" ,count)    

print("--------------------")

from math import *
def countDigits (num):
    return int(log10(num)+1)
x=int(input("enter a no.: "))
print("no. of digits: ",countDigits(x))
