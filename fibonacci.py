def func (num):
    if num==0 or num==1:
        return num
    return func(num-1)+func(num-2)
def fib_no(n):
    answer=func(n)
    return answer
n=6
print(fib_no(n))