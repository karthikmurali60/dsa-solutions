# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, root, subRoot):
        if root is None or subRoot is None:
            return root == subRoot
        
        return root.val == subRoot.val and self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)          
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            return None
        
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        
        leftTree = self.isSubtree(root.left, subRoot)
        rightTree = self.isSubtree(root.right, subRoot)
        
        return leftTree or rightTree
        