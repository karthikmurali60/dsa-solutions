class Solution:
    def backtrack(self, index, dp):
        if index < 0:
            return 0
        if index == 0:
            return 1
        
        if dp[index] != -1:
            return dp[index]
        
        dp[index] = self.backtrack(index - 2, dp) + self.backtrack(index - 1, dp)
        
        return dp[index]
    
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        
        return self.backtrack(n, dp)