"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def narypostorder(self, root, result):
        if root is None:
            return
        
        for i in range(len(root.children)):
            self.narypostorder(root.children[i], result)
            
        result.append(root.val)
        
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        
        self.narypostorder(root, result)
        
        return result
