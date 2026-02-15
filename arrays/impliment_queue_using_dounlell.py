class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def is_empty(self):
        return self.head is None
    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return temp.data
    def front(self):
        if self.is_empty():
            return None
        return self.head.data
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue()) 
print(q.front())    
