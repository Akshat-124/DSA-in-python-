def nextGreaterElements(nums):
    n = len(nums)
    result = [-1] * n
    stack = []   
    for i in range(2 * n - 1, -1, -1):
        index = i % n
        while stack and nums[stack[-1]] <= nums[index]:
            stack.pop()
        if i < n:
            if stack:
                result[index] = nums[stack[-1]]
        stack.append(index)
    return result
nums = [1, 2, 1]
print(nextGreaterElements(nums))