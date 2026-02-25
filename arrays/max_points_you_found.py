def maxScore(cardPoints, k):
    n = len(cardPoints)
    if k == n:
        return sum(cardPoints)
    total_sum = sum(cardPoints)
    window_size = n - k
    current_sum = sum(cardPoints[:window_size])
    min_subarray_sum = current_sum
    for i in range(window_size, n):
        current_sum += cardPoints[i]
        current_sum -= cardPoints[i - window_size]
        min_subarray_sum = min(min_subarray_sum, current_sum)
    return total_sum - min_subarray_sum
cardPoints = [1,2,3,4,5,6,1]
k = 3

print(maxScore(cardPoints, k))