class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.min_stack[-1]
obj = MinStack()
obj.push(5)
print("Pushed 5")
print("Current Min:", obj.getMin())   
obj.push(3)
print("Pushed 3")
print("Current Min:", obj.getMin())   
obj.push(7)
print("Pushed 7")
print("Current Min:", obj.getMin())   
obj.push(2)
print("Pushed 2")
print("Current Min:", obj.getMin())   
print("Top Element:", obj.top())     
obj.pop()
print("Popped top element")
print("Current Min:", obj.getMin())   
obj.pop()
print("Popped top element")
print("Current Min:", obj.getMin())