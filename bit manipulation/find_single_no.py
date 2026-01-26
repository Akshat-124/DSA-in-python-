def single_number(arr):          #bruteforce , TC=o(n),SC=o(n/2)
    hash_map = {}
    for num in arr:
        hash_map[num] = hash_map.get(num, 0) + 1
    for key in hash_map:
        if hash_map[key] == 1:
            return key
arr = [5, 1, 3, 3, 7, 1, 7]
print(single_number(arr))  

print("------------------")

def single_number(arr):            #optimal , TC=o(n),SC=o(1)
    result = 0
    for num in arr:
        result ^= num
    return result
arr = [5, 1, 3, 3, 7, 1, 7]
print(single_number(arr))  