class Solution:
    def canCross(self, stones: List[int]) -> bool:
        vis = set()
        
        queue = [(0, 0)]
        
        while queue:
            pos, jump = queue.pop(0)
            
            if (pos, jump) in vis:
                continue
                
            vis.add((pos, jump))
            
            if pos == stones[-1]:
                return True
            
            for i in range(jump - 1, jump + 2):
                if i <= 0:
                    continue
                
                if pos + i in stones:
                    queue.append((pos + i, i))
                    
        return False