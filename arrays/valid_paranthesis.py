def isValid(s: str) -> bool:
    stack = []
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for char in s:
        if char in mapping.values():
            stack.append(char)
        else:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack) == 0
print(isValid("()"))        
print(isValid("()[]{}"))   
print(isValid("(]"))        
print(isValid("([)]"))      
print(isValid("{[]}"))      
