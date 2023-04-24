# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        
        if left is None or right is None:
            return False
        
        if left.val != right.val:
            return False
        
        outerNodes = self.isMirror(left.left, right.right)
        innerNodes = self.isMirror(left.right, right.left)
        
        return outerNodes and innerNodes        
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.isMirror(root.left, root.right)
