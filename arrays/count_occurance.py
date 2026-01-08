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
    ub = len(nums)

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1

    return ub


def countOccurrence(nums, target):
    lb = lowerBound(nums, target)

    if lb == -1 or nums[lb] != target:
        return 0

    ub = upperBound(nums, target)
    return ub - lb
nums = [1, 2, 2, 2, 3, 4, 5]
target = 2

print(countOccurrence(nums, target))
