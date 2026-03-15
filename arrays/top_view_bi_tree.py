from collections import deque
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
def topView(root):
    if root is None:
        return
    q = deque()
    mp = {}   
    q.append((root, 0))
    while q:
        node, hd = q.popleft()
        if hd not in mp:
            mp[hd] = node.data
        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))
    for key in sorted(mp):
        print(mp[key], end=" ")
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.right.right = Node(5)
root.right.right.left = Node(6)
topView(root)