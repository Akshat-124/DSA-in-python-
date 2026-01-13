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
    def middle(self):                    ########bruteforce######## leetcode=876 tc=o(n+n/2)
        n=0
        temp=self.head
        while temp is not None:
            n+=1
            temp=temp.next
        temp=self.head
        for i in range (0,n//2):
            temp=temp.next
        return temp
sll=SinglyLinkedList()
sll.append(100)
sll.append(200)
sll.append(300)
sll.append(400)
sll.append(500)
mid=sll.middle()
print(mid.val)

print("---------------------------------------------------")

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
    def middle(self):                                   ###########optimal###########   tc=o(n/2)
        n=0
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow
sll=SinglyLinkedList()
sll.append(100)
sll.append(200)
sll.append(300)
sll.append(400)
sll.append(500)
mid=sll.middle()
print(mid.val)


