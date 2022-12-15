class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left, right = 0, len(colors) - 1
        maxDist = 0
        
        while left < right:
            if colors[left] != colors[right]:
                maxDist = max(maxDist, abs(left - right))
            
            left += 1
            
        left, right = 0, len(colors) - 1
        while left < right:
            if colors[left] != colors[right]:
                maxDist = max(maxDist, abs(left - right))
            
            right -= 1
            
        return maxDist