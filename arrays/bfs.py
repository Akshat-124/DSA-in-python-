from collections import deque
class TreeNode:
 def __init__(self,val):
  self.val=val
  self.left=None
  self.right=None
def rightSideView(root):
 if not root:return []
 q=deque([root])
 ans=[]
 while q:
  n=len(q)
  for i in range(n):
   node=q.popleft()
   if i==n-1:ans.append(node.val)
   if node.left:q.append(node.left)
   if node.right:q.append(node.right)
 return ans
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(5)
root.right.right=TreeNode(4)
print(rightSideView(root))