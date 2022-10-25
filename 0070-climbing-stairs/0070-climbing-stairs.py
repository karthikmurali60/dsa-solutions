class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        prev1, prev2, curr = 1, 1, 0
        
        for i in range(2, n + 1):
            left = prev2
            right = prev1
            
            curr = left + right
            prev2 = prev1
            prev1 = curr
        
        return curr
            