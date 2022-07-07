# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorderTraversal = []

        if root:
            inorderTraversal += self.inorderTraversal(root.left)
            inorderTraversal.append(root.val)
            inorderTraversal += self.inorderTraversal(root.right)

        return inorderTraversal
