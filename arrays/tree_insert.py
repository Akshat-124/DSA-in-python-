class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
    def insert(self, data):
        new_node = Node(data)
        queue = []
        queue.append(self.root)
        while queue:
            temp = queue.pop(0)
            if temp.left is None:
                temp.left = new_node
                return
            else:
                queue.append(temp.left)
            if temp.right is None:
                temp.right = new_node
                return
            else:
                queue.append(temp.right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)
    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")
tree = BinaryTree(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
print("Inorder Traversal:")
tree.inorder(tree.root)
print("\nPreorder Traversal:")
tree.preorder(tree.root)
print("\nPostorder Traversal:")
tree.postorder(tree.root)