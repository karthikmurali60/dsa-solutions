# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root):
        if root is None:
            return 0
        
        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)
        
        if leftDepth == -1 or rightDepth == -1:
            return -1
        
        if abs(leftDepth - rightDepth) > 1:
            return -1
        
        return 1 + max(leftDepth, rightDepth)
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.depth(root) != -1:
            return True
        
        return False
