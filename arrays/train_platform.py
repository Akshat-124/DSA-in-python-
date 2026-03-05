def minPlatforms(arr, dep):
    n = len(arr)
    ans = 1
    for i in range(n):
        count = 1
        for j in range(n):
            if i != j:
                if arr[i] >= arr[j] and arr[i] <= dep[j]:
                    count += 1
        ans = max(ans, count)
    return ans
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(minPlatforms(arr, dep))