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
    def delete(self,val):
        temp=self.head
        if temp.next is not None:
            if temp.val==val:
                self.head=temp.next
                return 
            else:
                found=False
                prev=None
                while temp is not None:
                    if temp.val==val:
                        found=True
                        break
                    prev=temp
                    temp=temp.next
                if found:
                    prev.next=temp.next
                    return
                else:
                    print("node not found")
    def display(self):
        curr=self.head
        while curr:
            print(curr.val , end=" ")
            curr=curr.next
        print("none")
sll=SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(25)
sll.append(30)
sll.delete(25)
sll.display()