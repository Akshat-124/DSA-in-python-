class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def del_dupli(self):
        curr = self.head
        while curr and curr.next:
            if curr.data == curr.next.data:
                nxt = curr.next
                curr.next = nxt.next
                if nxt.next:
                    nxt.next.prev = curr
            else:
                curr = curr.next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
dll = DoublyLinkedList()

dll.append(1)
dll.append(2)
dll.append(2)
dll.append(3)
dll.append(3)
dll.append(6)

print("Before removing duplicates:")
dll.print_list()

dll.del_dupli()

print("After removing duplicates:")
dll.print_list()








                
