class Stack:
    def __init__(self):                  #optimal,TC=O(1)
        self.stack = []   
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")
    def pop(self):
        if self.isEmpty():
            print("Stack Underflow! Stack is empty.")
            return None
        return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            print("Stack is empty.")
            return None
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    def display(self):
        print("Stack:", self.stack)
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
print("Top element:", s.peek())
print("Popped:", s.pop())
s.display()
print("Stack size:", s.size())
