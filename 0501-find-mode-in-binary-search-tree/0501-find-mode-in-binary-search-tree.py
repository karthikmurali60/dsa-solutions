# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root, inorder):
        if root is None:
            return
        
        self.inorderTraversal(root.left, inorder)
        
        if root.val in inorder:
            inorder[root.val] += 1
        else:
            inorder[root.val] = 1
        
        self.inorderTraversal(root.right, inorder)
        
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        inorder = {}
        
        self.inorderTraversal(root, inorder)
        
        result = []
        maxVal = 0
        
        for val in inorder.values():
           maxVal = max(val, maxVal)
        
        for key, val in inorder.items():
            if val == maxVal:
                result.append(key)
                
        return result