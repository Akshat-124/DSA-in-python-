class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.front = 0
        self.rear = -1
        self.capacity = capacity
    def is_empty(self):
        return self.front > self.rear
    def is_full(self):
        return len(self.queue) == self.capacity
    def enqueue(self, x):
        if self.is_full():
            print("Queue Overflow! Cannot insert", x)
            return
        self.queue.append(x)
        self.rear += 1
        print(f"Enqueued: {x}")
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Nothing to remove")
            return None
        removed = self.queue[self.front]
        self.front += 1
        print(f"Dequeued: {removed}")
        return removed
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue[self.front]
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue:", self.queue[self.front:self.rear+1])
q = Queue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()        
print("Front:", q.peek())  
q.dequeue()
q.display()        
