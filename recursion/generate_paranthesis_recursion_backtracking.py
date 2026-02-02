def generateParentheses_bruteforce(n):                     #bruteforce
    result = []
    def is_valid(s):
        balance = 0
        for ch in s:
            if ch == "(":
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0
    def generate_all(curr):
        if len(curr) == 2 * n:
            if is_valid(curr):
                result.append(curr)
            return
        generate_all(curr + "(")
        generate_all(curr + ")")
    generate_all("")
    return result
print(generateParentheses_bruteforce(3))

print("--------------------------------")

def generateParentheses_optimal(n):                          #optimal
    result = []
    def backtrack(curr, open_count, close_count):
        if len(curr) == 2 * n:
            result.append(curr)
            return
        if open_count < n:
            backtrack(curr + "(", open_count + 1, close_count)
        if close_count < open_count:
            backtrack(curr + ")", open_count, close_count + 1)
    backtrack("", 0, 0)
    return result
print(generateParentheses_bruteforce(3))

