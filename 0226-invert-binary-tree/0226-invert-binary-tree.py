# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invert(self, root):
        if root is None:
            return None
        
        if root.left is None and root.right is None:
            return root
        
        root.left, root.right = root.right, root.left
        
        self.invert(root.left)
        self.invert(root.right)
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        
        return root