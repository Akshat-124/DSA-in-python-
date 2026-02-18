def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0
def infix_to_postfix(expression):
    stack = []
    result = ""
    for ch in expression:
        if ch.isalnum():
            result += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(ch):
                result += stack.pop()
            stack.append(ch)
    while stack:
        result += stack.pop()
    return result
expr1 = "A+B*C"
print("Infix :", expr1)
print("Postfix:", infix_to_postfix(expr1))
print()
expr2 = "(A+B)*C"
print("Infix :", expr2)
print("Postfix:", infix_to_postfix(expr2))
print()
expr3 = "A+B*C-D"
print("Infix :", expr3)
print("Postfix:", infix_to_postfix(expr3))

