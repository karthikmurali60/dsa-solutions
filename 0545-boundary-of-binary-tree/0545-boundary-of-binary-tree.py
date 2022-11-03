# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isLeaf(self, root):
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            return True
        
        return False
    
    def traverseLeft(self, root, result):
        curr = root.left
        
        while curr:
            if not self.isLeaf(curr):
                result.append(curr.val)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
    
    def traverseLeaves(self, root, result):
        if root is None:
            return None
        
        if self.isLeaf(root):
            result.append(root.val)
        
        self.traverseLeaves(root.left, result)
        self.traverseLeaves(root.right, result)
        
    def traverseRightInReverse(self, root, result):
        temp = []
        
        curr = root.right
        
        while curr:
            if not self.isLeaf(curr):
                temp.append(curr.val)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
                
        for i in range(len(temp) - 1, -1, -1):
            result.append(temp[i])
        
    
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        if not self.isLeaf(root):
            result.append(root.val)
            
        self.traverseLeft(root, result)
        self.traverseLeaves(root, result)
        self.traverseRightInReverse(root, result)
            
        return result