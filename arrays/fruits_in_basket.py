#brute
def totalFruit(fruits):
    n = len(fruits)
    max_len = 0
    for i in range(n):
        fruit_set = set()
        for j in range(i, n):
            fruit_set.add(fruits[j])
            if len(fruit_set) > 2:
                break
            max_len = max(max_len, j - i + 1)
    return max_len
print(totalFruit([1,2,1]))          
print(totalFruit([0,1,2,2]))        

print("-------------")

#better
def totalFruit(fruits):
    n = len(fruits)
    max_len = 0
    for i in range(n):
        freq = {}
        for j in range(i, n):
            freq[fruits[j]] = freq.get(fruits[j], 0) + 1
            if len(freq) > 2:
                break
            max_len = max(max_len, j - i + 1)
    return max_len
print(totalFruit([1,2,1]))          
print(totalFruit([0,1,2,2])) 

print("--------------")

#optimal
def totalFruit(fruits):
    left = 0
    max_len = 0
    freq = {}
    for right in range(len(fruits)):
        freq[fruits[right]] = freq.get(fruits[right], 0) + 1
        while len(freq) > 2:
            freq[fruits[left]] -= 1
            if freq[fruits[left]] == 0:
                del freq[fruits[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
print(totalFruit([1,2,1]))        
print(totalFruit([0,1,2,2]))      
print(totalFruit([1,2,3,2,2]))    