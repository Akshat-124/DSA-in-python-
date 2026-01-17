class Node:                      #brute force    TC=o(n),SC=o(n)
    def __init__(self,val):
        self.val=val
        self.next=next
def cycle(head):
    temp=head
    my_dict={}
    travel=0
    while temp is not None:
        if temp in my_dict:
            return travel-my_dict[temp]
        my_dict[temp]=travel
        travel+=1
        temp=temp.next
    return 0
n1=Node(3)
n2=Node(2)
n3=Node(0)
n4=Node(-4)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n2
print(cycle(n1))

print("------------")

class Node:                      #optimal     TC=o(n),SC=o(1)
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
            slow=slow.next
            count=1
            while slow!=fast:
                slow=slow.next
                count+=1
            return count
    return 0
n1=Node(3)
n2=Node(2)
n3=Node(0)
n4=Node(-4)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n2
print(cycle(n1))