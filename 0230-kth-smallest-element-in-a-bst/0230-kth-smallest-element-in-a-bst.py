# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root, inorder):
        if root is None:
            return None
        
        self.inorderTraversal(root.left, inorder)
        inorder.append(root.val)
        self.inorderTraversal(root.right, inorder)       
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        
        self.inorderTraversal(root, inorder)
        
        return inorder[k - 1]