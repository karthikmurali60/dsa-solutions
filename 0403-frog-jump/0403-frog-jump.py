class Solution:
    def canCross(self, stones: List[int]) -> bool:
        seen = set()
        
        n = len(stones)
        
        queue = [(0, 0)]
        
        while queue:
            loc, jump = queue.pop(0)
            
            if (loc, jump) in seen:
                continue
                
            seen.add((loc, jump))
            
            if loc == stones[n - 1]:
                return True
            
            if loc < stones[-1]:
                for i in range(jump - 1, jump + 2):
                    if i <= 0:
                        continue
                    if loc + i in stones:
                        queue.append((loc + i, i))

        return False
            