# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, sums, k):
        if root is None:
            return None
        
        if k - root.val in sums:
            return True
        
        if root.val not in sums:
            sums[root.val] = 1
        
        leftTree = self.dfs(root.left, sums, k)
        rightTree = self.dfs(root.right, sums, k)
        
        return leftTree or rightTree        
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        sums = {}
        
        return self.dfs(root, sums, k)
        