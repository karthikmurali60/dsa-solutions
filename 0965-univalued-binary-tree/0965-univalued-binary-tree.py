# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkValues(self, root, val):
        if root is None:
            return True
        
        if root.val != val:
            return False
        
        return self.checkValues(root.left, val) and self.checkValues(root.right, val)
        
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return self.checkValues(root, root.val)