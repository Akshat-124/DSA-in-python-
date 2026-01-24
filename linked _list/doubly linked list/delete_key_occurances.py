class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    def del_key(self,key):
        if self.head is None and self.head.val==key:
            return None
        temp=self.head
        prev=None
        new_head=self.head
        while temp is not None:
            if temp.data==key:
                if prev is not None:
                    prev.next=temp.next
                if prev.next is not None:
                    temp.next.prev=prev
                if temp==new_head:
                    new_head=new_head.next
            prev=temp
            temp=temp.next
        return new_head
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
dll = DoublyLinkedList()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_end(40)
dll.insert_end(30)
dll.del_key(30)
dll.display()
