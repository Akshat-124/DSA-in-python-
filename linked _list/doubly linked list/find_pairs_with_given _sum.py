class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
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
    def sum_pairs(self,target):                #bruteforce TC=o(n^2),SC=o(1)
        temp1=self.head
        result=[]
        while temp1 is not None:
            temp2=temp1.next
            while temp2 is not None:
                if temp1.data + temp2.data == target:
                    result.append([temp1.data,temp2.data])
                temp2=temp2.next
            temp1=temp1.next
        return result
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
dll = DoublyLinkedList()
dll.insert_end(1)
dll.insert_end(2)
dll.insert_end(4)
dll.insert_end(5)
dll.insert_end(6)
dll.insert_end(8)
dll.insert_end(9)
print(dll.sum_pairs(7))
dll.display()   

print("------------------------------")

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
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
    def sum_pair(self,target):             #better sol TC=o(n),SC=o(n)
        my_set=set()
        temp=self.head
        result=[]
        while temp is not None:
            remaining=target-temp.data
            if remaining in my_set:
                result.append([remaining,temp.data])
            my_set.add(temp.data)
            temp=temp.next
        return result
dll = DoublyLinkedList()
dll.insert_end(1)
dll.insert_end(2)
dll.insert_end(4)
dll.insert_end(5)
dll.insert_end(6)
dll.insert_end(8)
dll.insert_end(9)
print(dll.sum_pair(7))    

print("--------------------------")

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
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
    def sum_pair(self,target):            #optimal TC=o(n),SC=o(1)
        result=[]
        left=self.head
        right=self.head
        while right.next is not None:
            right=right.next
        while left is not None and right is not None and left.data<right.data:
            total=left.data+right.data
            if total==target:
                result.append([left.data,right.data])
                left=left.next
                right=right.prev
            elif total>target:
                right=right.prev
            else:
                left=left.next
        return result
dll = DoublyLinkedList()
dll.insert_end(1)
dll.insert_end(2)
dll.insert_end(4)
dll.insert_end(5)
dll.insert_end(6)
dll.insert_end(8)
dll.insert_end(9)
print(dll.sum_pair(7))  
