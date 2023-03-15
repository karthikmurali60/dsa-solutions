class Solution:
    def canCross(self, stones: List[int]) -> bool:
        seen = set()
        
        queue = [(0, 0)]
        
        while queue:
            loc, steps = queue.pop()
            
            if (loc, steps) in seen:
                continue
                
            seen.add((loc,steps))
            
            # reached the last stone
            if loc == stones[-1]:
                return True
            
            elif loc < stones[-1]:
                for i in range(steps - 1, steps + 2):
                    if i <= 0:
                        continue
                    
                    if loc + i in stones:
                        queue.append((loc + i, i))
                        
        return False