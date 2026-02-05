def subset_sums(arr):            #optimal,TC=o(2^n),SC=o(2^n)
    result = []
    def backtrack(index, current_sum):
        if index == len(arr):
            result.append(current_sum)
            return
        backtrack(index + 1, current_sum + arr[index])
        backtrack(index + 1, current_sum)
    backtrack(0, 0)
    return result
arr = [1, 2, 3]
print(subset_sums(arr))
