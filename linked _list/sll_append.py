class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def append (self,val):
        new_node=Node(val)
        if self.head == None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
        