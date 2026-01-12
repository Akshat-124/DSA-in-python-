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
    def insert_at(self,val,pos):              #inserting                 #tc=o(n)
        new_node=Node(val)
        if pos==0:
            new_node.next=self.head
            self.head=new_node
        else:
            curr=self.head
            prev_node=None
            count=0
            while curr is not None and count<pos-1:
                prev_node=curr
                curr=curr.next
                count+=1
            prev_node.next=new_node
            new_node.next=curr
    def display(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
sll=SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(40)
sll.append(3)
sll.insert_at(30,2)
sll.display()