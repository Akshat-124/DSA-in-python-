from collections import deque
class StackUsingQueue:
    def __init__(self):
        self.q = deque()
    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.q.popleft()
    def top(self):
        if self.is_empty():
            return "Stack is empty"
        return self.q[0]
    def is_empty(self):
        return len(self.q) == 0
s = StackUsingQueue()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())  
print(s.top())  

print("------------------")

from collections import deque
class StackUsingTwoQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    def push(self, x):
        self.q1.append(x)
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        popped = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return popped
    def top(self):
        if self.is_empty():
            return "Stack is empty"
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top_element = self.q1.popleft()
        self.q2.append(top_element)
        self.q1, self.q2 = self.q2, self.q1
        return top_element
    def is_empty(self):
        return len(self.q1) == 0
s = StackUsingTwoQueues()
s.push(5)
s.push(15)
s.push(25)
print(s.pop())  # 25
print(s.top())  # 15
