a = 5
b = 10
print("Before:")
print("a =", a, "b =", b)
a = a ^ b    #xor
b = a ^ b
a = a ^ b
print("After:")
print("a =", a, "b =", b)
