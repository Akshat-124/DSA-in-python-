def combinationSum(candidates, target):
    result = []
    def backtrack(start, current_sum, path):
        if current_sum == target:
            result.append(path.copy())
            return
        if current_sum > target:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, current_sum + candidates[i], path)  
            path.pop()  
    backtrack(0, 0, [])
    return result
candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))

