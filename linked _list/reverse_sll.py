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
    def reverse(self):                         ##reverse## bryteforce TC=o(n),SC=o(n)
        temp=self.head
        stack=[]
        while temp is not None:
            stack.append(temp.val)
            temp=temp.next
        temp=self.head
        while temp is not None:
            e=stack.pop()
            temp.val=e
            temp=temp.next
        return self.head
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")
sll=SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(25)
sll.append(30)
sll.reverse()
sll.display()

print("----------------------------------")

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
    def reverse(self):                   ##reverse## optimal sol , TC=o(n),SC=o(1)
        temp=self.head
        prev=None
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        return self.head
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")
sll=SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(25)
sll.append(30)
sll.reverse()
sll.display()