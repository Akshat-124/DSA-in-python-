class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return True, -1
            left_balanced, left_height = dfs(node.left)
            if not left_balanced:
                return False, 0  
            right_balanced, right_height = dfs(node.right)
            if not right_balanced:
                return False, 0  
            balanced = abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            return balanced, height
        return dfs(root)[0]
from collections import deque
def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root
sol = Solution()
root1 = build_tree([3, 9, 20, None, None, 15, 7])
print("Test 1:", sol.isBalanced(root1))  
root2 = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
print("Test 2:", sol.isBalanced(root2))  
root3 = build_tree([])
print("Test 3:", sol.isBalanced(root3))  
root4 = build_tree([1])
print("Test 4:", sol.isBalanced(root4))  