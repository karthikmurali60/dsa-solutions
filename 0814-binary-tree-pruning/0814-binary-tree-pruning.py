# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def containsOne(self, root):
        if root is None:
            return False
        
        if root.val == 1:
            return True
        
        right = self.containsOne(root.right)
        left = self.containsOne(root.left)
        
        return (right or left)
            
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        curr = root
        
        if curr.left:
            if not self.containsOne(curr.left):
                curr.left = None
            else:
                self.pruneTree(curr.left)
        if curr.right:
            if not self.containsOne(curr.right):
                curr.right = None
            else:
                self.pruneTree(curr.right)
                
        if root.left is None and root.right is None and root.val == 0:
            return None
                
        return root