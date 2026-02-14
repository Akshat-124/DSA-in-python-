class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self, x):
        self.stack1.append(x)
    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                return "Queue is Empty"
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    def front(self):
        if not self.stack2:
            if not self.stack1:
                return "Queue is Empty"
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0
q = QueueUsingStack()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.dequeue())  
print(q.front())    
print(q.dequeue())  
print(q.is_empty()) 