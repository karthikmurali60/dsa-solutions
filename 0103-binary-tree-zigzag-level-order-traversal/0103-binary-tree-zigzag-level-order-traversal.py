# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = [root]
        rev = False
        result = []
        
        while queue:
            size = len(queue)
            ans = [None] * size
            
            for i in range(size):
                ele = queue.pop(0)
                index = size - i - 1 if rev else i 
                ans[index] = ele.val
                
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)

            result.append(ans)
            rev = not rev
            
        return result
