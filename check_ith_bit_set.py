N = 13
i = 1

if (N & (1 << i)) != 0:  #left shift one time then & operator
    print("SET")
else:
    print("NOT SET")
