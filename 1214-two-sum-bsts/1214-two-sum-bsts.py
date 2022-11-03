# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, sums):
        if root is None:
            return None
        
        sums[root.val] = 1
        self.dfs(root.left, sums)
        self.dfs(root.right, sums)
        
    def checkTwoSum(self, root, sums, target):
        if root is None:
            return None
        
        if target - root.val in sums:
            return True
        
        leftTree = self.checkTwoSum(root.left, sums, target)
        rightTree = self.checkTwoSum(root.right, sums, target)
        
        return leftTree or rightTree
        
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        sums = {}
        
        self.dfs(root1, sums)
                
        return self.checkTwoSum(root2, sums, target)