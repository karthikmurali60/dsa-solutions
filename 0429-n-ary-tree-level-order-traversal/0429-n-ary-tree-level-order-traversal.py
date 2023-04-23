"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        
        if len(root.children) == 0:
            return [[root.val]]
        
        queue = [root]
        
        answer = []
        
        while queue:
            size = len(queue)
            temp = []
            
            for i in range(size):
                ele = queue.pop(0)
                
                temp.append(ele.val)
                
                for i in range(len(ele.children)):
                    queue.append(ele.children[i])
                    
            answer.append(temp)
            
        return answer
