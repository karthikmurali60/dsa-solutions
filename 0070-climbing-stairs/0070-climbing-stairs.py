class Solution:
    def dfs(self, index, dp):
        if index == 0:
            return 1
        
        if dp[index] != -1:
            return dp[index]
        
        oneStep = self.dfs(index - 1, dp)
        
        twoStep = 0
        if index > 1:
            twoStep = self.dfs(index - 2, dp)
            
        dp[index] = oneStep + twoStep
        
        return oneStep + twoStep
        
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        
        return self.dfs(n, dp)