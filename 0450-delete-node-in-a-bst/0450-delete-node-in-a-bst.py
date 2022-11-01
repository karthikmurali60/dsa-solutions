# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLastRightChild(self, node):
        if node.right is None:
            return node
        
        return self.findLastRightChild(node.right)
    
    def transform(self, node):
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            rightChild = node.right
            lastRightChild = self.findLastRightChild(node.left)
            lastRightChild.right = rightChild
            return node.left        
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if root.val == key:
            return self.transform(root)
        
        curr = root
        while curr:
            if curr.val > key:
                if curr.left and curr.left.val == key:
                    curr.left = self.transform(curr.left)
                    break
                else:
                    curr = curr.left                   
            elif curr.val < key:
                if curr.right and curr.right.val == key:
                    curr.right = self.transform(curr.right)
                    break
                else:
                    curr = curr.right

        return root
                
                
            