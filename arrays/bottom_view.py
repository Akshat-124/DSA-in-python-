from collections import deque
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
def bottomView(root):
    if root is None:
        return []
    q = deque()
    hd_map = {}
    q.append((root, 0))   

    while q:
        node, hd = q.popleft()
        hd_map[hd] = node.data
        if node.left:
            q.append((node.left, hd - 1))
        if node.right:
            q.append((node.right, hd + 1))
    ans = []
    for i in sorted(hd_map):
        ans.append(hd_map[i])
    return ans
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
print(bottomView(root))