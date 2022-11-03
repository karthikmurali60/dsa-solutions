# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, totalSum, low, high):
        if root is None:
            return 0
        
        if low <= root.val and root.val <= high:
            self.totalSum += root.val
        
        self.dfs(root.left, self.totalSum, low, high)
        self.dfs(root.right, self.totalSum, low, high)
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.totalSum = 0
        
        self.dfs(root, self.totalSum, low, high)
        
        return self.totalSum