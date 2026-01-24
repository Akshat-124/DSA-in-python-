N = 13
i = 2
result = N & ~(1 << i)   #lest shift 2 times of 1 then inverse~ the value then take & with 13
print(result)
