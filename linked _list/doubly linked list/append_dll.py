class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def append(self,val):           #append TC=o(n),SC=o(1)
        new_node=Node(val)
        if not self.head:
            self.head=new_node
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=new_node
            new_node.prev=curr
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

dll=DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.display()