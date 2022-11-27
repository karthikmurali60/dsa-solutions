# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, inord):
        if root is None:
            return root
        
        self.inorder(root.left, inord)
        inord.append(root.val)
        self.inorder(root.right, inord)
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        in1, in2 = [], []
        result = []
        
        self.inorder(root1, in1)
        self.inorder(root2, in2)
        
        i1, i2 = 0, 0
        
        while i1 < len(in1) and i2 < len(in2):
            if in1[i1] < in2[i2]:
                result.append(in1[i1])
                i1 += 1
            else:
                result.append(in2[i2])
                i2 += 1
                
        while i1 < len(in1):
            result.append(in1[i1])
            i1 += 1
        
        while i2 < len(in2):
            result.append(in2[i2])
            i2 += 1
            
        return result    
        