def armstrong (num):
    n=num
    total=0
    nod=len(str(n))
    while num>0 :
        ld=num%10
        total=total+(ld**nod)
        num=num//10
    return total==n
n = int(input("enter a number: "))
result = armstrong(n)
print (result)