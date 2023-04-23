# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return [[root.val]]
        
        queue = [root]
        
        answer = []
        
        while queue:
            size = len(queue)
            temp = []
            
            for i in range(size):
                ele = queue.pop(0)
                
                temp.append(ele.val)
                
                if ele.left:
                    queue.append(ele.left)
                    
                if ele.right:
                    queue.append(ele.right)
                    
            answer.append(temp)
            
        return answer
