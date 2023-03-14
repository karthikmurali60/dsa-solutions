# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxSum = -1e9
        
    def findMaxSum(self, node, maxSum):
        if node is None:
            return 0
        
        leftSum = max(0, self.findMaxSum(node.left, self.maxSum))
        rightSum = max(0, self.findMaxSum(node.right, self.maxSum))
        
        self.maxSum = max(self.maxSum, leftSum + rightSum + node.val)
        
        return node.val + max(leftSum, rightSum)
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:        
        self.findMaxSum(root, self.maxSum)
        
        return self.maxSum