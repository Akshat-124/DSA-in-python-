n=16
result = n & (n-1)
if result==0:
    print(True)
False

print("----------")

n=13
result = n & (n-1)
if n==0:
    print(True)
if result==0:
    print(True)
print(False)
