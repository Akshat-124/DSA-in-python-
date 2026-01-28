def generate_subsequences(arr):                                 #bruteforce,TC=o(n*2^n)
    n = len(arr)
    result = []
    for mask in range(1 << n):  # 0 to 2^n - 1
        subseq = []
        for i in range(n):
            if mask & (1 << i):
                subseq.append(arr[i])
        result.append(subseq)
    return result
arr = [1, 2, 3]
print(generate_subsequences(arr))

print("---------------------")

def generate_subsequences_recursive(arr, index, curr, result):    #optimal,TC=o(2^n),SC=o(n)
    if index == len(arr):
        result.append(curr.copy())
        return
    curr.append(arr[index])
    generate_subsequences_recursive(arr, index + 1, curr, result)
    curr.pop()
    generate_subsequences_recursive(arr, index + 1, curr, result)
arr = [1, 2, 3]
result = []
generate_subsequences_recursive(arr, 0, [], result)

print(result)


