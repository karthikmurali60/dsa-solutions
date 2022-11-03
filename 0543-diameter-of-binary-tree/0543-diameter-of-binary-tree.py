# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def findDiameter(self, root, maxDiameter):
        if root is None:
            return 0
        
        lh = self.findDiameter(root.left, self.maxDiameter)
        rh = self.findDiameter(root.right, self.maxDiameter)
        
        self.maxDiameter = max(self.maxDiameter, lh + rh)
        
        return 1 + max(lh, rh)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:     
        self.maxDiameter = 0

        self.findDiameter(root, self.maxDiameter)
        
        return self.maxDiameter