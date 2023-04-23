"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def narypreorder(self, root, result):
        if root is None:
            return
        
        result.append(root.val)
        
        for i in range(len(root.children)):
            self.narypreorder(root.children[i], result)
        
        
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        
        self.narypreorder(root, result)
        
        return result
