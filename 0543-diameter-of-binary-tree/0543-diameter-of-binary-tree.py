# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDiameter(self, root, diameter):
        if root is None:
            return 0
        
        leftDepth = self.findDiameter(root.left, self.diameter)
        rightDepth = self.findDiameter(root.right, self.diameter)
        
        self.diameter = max(self.diameter, leftDepth + rightDepth)
        
        return 1 + max(leftDepth, rightDepth)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        self.findDiameter(root, self.diameter)
        
        return self.diameter
