# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMax(self, root):
        if root is None:
            return 0
        
        leftSum = max(0, self.findMax(root.left))
        rightSum = max(0, self.findMax(root.right))
        
        self.pathSum = max(self.pathSum, leftSum + rightSum + root.val)
        
        return root.val + max(leftSum, rightSum)
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.pathSum = -1e9
        
        self.findMax(root)
        
        return self.pathSum
