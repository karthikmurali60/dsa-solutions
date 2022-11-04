# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if root is None:
            return None
        
        self.dfs(root.right)
        
        temp = root.val
        root.val += self.currSum
        self.currSum += temp
        
        self.dfs(root.left)        
        
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.currSum = 0
        
        self.dfs(root)
        
        return root