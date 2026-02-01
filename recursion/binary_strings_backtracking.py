def generate_binary_bruteforce(n):         #bruteforce,tc=o(2^n*n)
    result = []
    for i in range(2**n):
        binary = bin(i)[2:]         
        binary = binary.zfill(n)     
        result.append(binary)
    return result
n = 3
print(generate_binary_bruteforce(n))

print("---------------------------------")

def generate_binary_optimal(n):             #optimal,tc=o(2^n)
    def solve(index, current):
        if index == n:
            print("".join(current))
            return
        current.append('0')
        solve(index + 1, current)
        current.pop()
        current.append('1')
        solve(index + 1, current)
        current.pop()
    solve(0, [])
generate_binary_optimal(3)

