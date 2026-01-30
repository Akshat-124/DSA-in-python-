def check_subsequence_sum(i, arr, k):
    if i == len(arr):                                #optimal ,TC=o(2^n), SC=o(n)
        return k == 0
    if arr[i] <= k:
        if check_subsequence_sum(i + 1, arr, k - arr[i]):
            return True
    if check_subsequence_sum(i + 1, arr, k):
        return True
    return False
arr = [1, 2, 1]
k = 2
print(check_subsequence_sum(0, arr, k))
