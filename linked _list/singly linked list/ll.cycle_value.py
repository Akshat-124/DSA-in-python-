class Node:                         #bruteforce      TC=o(n),SC=o(n)       ##########LC=142########
    def __init__(self,val):
        self.val=val
        self.next=next
def cycle(head):
    temp=head
    my_set=set()
    while temp is not None:
        if temp in my_set:
            return temp.val
        my_set.add(temp)
        temp=temp.next
    return False
n1=Node(3)
n2=Node(2)
n3=Node(0)
n4=Node(-4)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n2
print(cycle(n1))

print("----------")

class Node:                           #optimal      SC=o(1)
    def __init__(self,val):
        self.val=val
        self.next=next
def cycle(head):
    slow=head
    fast=head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            slow=head
            while slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow.val
    return None
n1=Node(3)
n2=Node(2)
n3=Node(0)
n4=Node(-4)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n2
print(cycle(n1))