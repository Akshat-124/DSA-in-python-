def count_subseq(index, curr_sum, arr, k):            #bruteforce,TC=o(2^n),SC=o(n)
    if index == len(arr):
        if curr_sum == k:
            return 1
        return 0
    take = count_subseq(index + 1, curr_sum + arr[index], arr, k)
    not_take = count_subseq(index + 1, curr_sum, arr, k)
    return take + not_take
arr = [1, 2, 1]
k = 2
print(count_subseq(0, 0, arr, k))

print("------------------")

def count_subarray_sum_k(arr, k):                     #optimal,TC=o(n),SC=o(n)
    prefix_sum = 0
    count = 0
    mp = {0: 1}
    for num in arr:
        prefix_sum += num
        if prefix_sum - k in mp:
            count += mp[prefix_sum - k]
        mp[prefix_sum] = mp.get(prefix_sum, 0) + 1
    return count
arr = [1, 2, 1]
k = 2
print(count_subarray_sum_k(arr, k))
