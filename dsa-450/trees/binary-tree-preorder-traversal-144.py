# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorderTraversal = []

        if root:
            preorderTraversal.append(root.val)
            preorderTraversal += self.preorderTraversal(root.left)
            preorderTraversal += self.preorderTraversal(root.right)

        return preorderTraversal
