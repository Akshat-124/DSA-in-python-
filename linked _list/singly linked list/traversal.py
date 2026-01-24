class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def append (self,val):           #append
        new_node=Node(val)
        if self.head == None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
    def traverse(self):             #traversing                               #tc=o(n)
        if not self.head:
            print("sll is empty")
        else:
            curr=self.head
            while curr is not None:
                print(curr.val,end=" ")
                curr=curr.next
            print()
sll=SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(40)
sll.append(3)
sll.traverse()

