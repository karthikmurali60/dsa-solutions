"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        maxDepth = 0
        
        for i in range(len(root.children)):
            maxDepth = max(maxDepth, self.maxDepth(root.children[i]))
        
        return 1 + maxDepth
    