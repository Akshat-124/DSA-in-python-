class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def push(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        return temp.data
    def peek(self):
        if self.is_empty():
            return None
        return self.head.data
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())   
print(s.peek())  
