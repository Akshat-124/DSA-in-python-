def lowerBound(nums, target):
    low, high = 0, len(nums) - 1
    lb = -1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1

    return lb


def upperBound(nums, target):
    low, high = 0, len(nums) - 1
    ub = -1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1

    return ub


def firstAndLastOccurrence(nums, target):
    lb = lowerBound(nums, target)

    if lb == -1 or nums[lb] != target:
        return [-1, -1]

    ub = upperBound(nums, target)

    if ub == -1:
        return [lb, len(nums) - 1]

    return [lb, ub - 1]
nums = [2, 4, 4, 4, 6, 8]
target = 4

print(firstAndLastOccurrence(nums, target))
