def combinationSum3(k, n):
    result = []
    def backtrack(start, k, target, path):
        if k == 0 and target == 0:
            result.append(path.copy())
            return
        if k == 0 or target < 0:
            return
        for num in range(start, 10):  
            path.append(num)
            backtrack(num + 1, k - 1, target - num, path)
            path.pop()  
    backtrack(1, k, n, [])
    return result
print(combinationSum3(3, 7))
