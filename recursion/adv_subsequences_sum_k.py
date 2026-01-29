def subsequence_sum_k(index, arr, curr, curr_sum, k):
    if index == len(arr):
        if curr_sum == k:                                   ##bruteforce TC=o(2^n)
            print(curr)
        return
    curr.append(arr[index])
    subsequence_sum_k(index + 1, arr, curr, curr_sum + arr[index], k)
    curr.pop()
    subsequence_sum_k(index + 1, arr, curr, curr_sum, k)
arr = [1, 2, 1]
k = 2
subsequence_sum_k(0, arr, [], 0, k)

print("----------------")

def subseq_one(index, arr, curr, curr_sum, k):              ##optimal TC=o(n)
    if index == len(arr):
        return curr_sum == k
    curr.append(arr[index])
    if subseq_one(index+1, arr, curr, curr_sum+arr[index], k):
        return True
    curr.pop()
    if subseq_one(index+1, arr, curr, curr_sum, k):
        return True
    return False
arr = [1, 2, 1]
k = 2
subsequence_sum_k(0, arr, [], 0, k)