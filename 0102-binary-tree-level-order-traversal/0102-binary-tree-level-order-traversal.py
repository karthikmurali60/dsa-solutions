# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        
        queue = [root]
        result = []
        
        while queue:
            ans = []
            size = len(queue)
            
            for i in range(size):
                ele = queue.pop(0)
                
                ans.append(ele.val)
                
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
                    
            result.append(ans)
            
        return result
            
            