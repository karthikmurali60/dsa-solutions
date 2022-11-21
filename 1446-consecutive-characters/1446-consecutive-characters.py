class Solution:
    def maxPower(self, s: str) -> int:
        count, maxCount = 0, 0
        left, right = 0, 0
        
        while right < len(s):
            if s[left] == s[right]:
                count += 1
            else:
                maxCount = max(maxCount, count)
                count = 1
                left = right
                
            right += 1
            
        maxCount = max(maxCount, count)
            
        return maxCount
        
        