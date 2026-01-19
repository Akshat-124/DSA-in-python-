class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_between(self,val,pos):         #insert_btw TC=o(n),SC=(1)
        new_node=Node(val)
        curr=self.head
        count=0
        while curr and count < pos-1:
            curr=curr.next
            count+=1
        if curr is None:
            print("pos out of bounds")
            return
        new_node.next=curr.next
        new_node.prev=curr
        if curr.next:
            curr.next.prev=new_node
        curr.next=new_node
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
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
dll=DoublyLinkedList()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_between(40,1)
dll.display()    