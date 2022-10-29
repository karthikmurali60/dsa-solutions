# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        
        queue, result = [], []
        queue.append(root)
        level = 0
        
        reverse = False
        
        while queue:
            size = len(queue)
            temp = [None] * size
            
            for i in range(size):
                ele = queue.pop(0)
                
                index = i if not reverse else (size - i - 1)
                temp[index] = ele.val
                
                if ele.left:
                    queue.append(ele.left)
                
                if ele.right:
                    queue.append(ele.right)
                    
            reverse = not reverse        
            result.append(temp)
            
        return result
            
                
            