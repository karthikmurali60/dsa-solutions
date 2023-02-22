class Solution:
    def dfs(self, index, cost, dp):
        if index < 0:
            return float('inf')
        
        if index == 0 or index == 1:
            return cost[index]
        
        if dp[index] != -1:
            return dp[index]
            
        dp[index] = cost[index] + min(self.dfs(index - 1, cost, dp), self.dfs(index - 2, cost, dp))
        
        return cost[index] + min(self.dfs(index - 1, cost, dp), self.dfs(index - 2, cost, dp))
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * (len(cost) + 1)
        
        return min(self.dfs(len(cost) - 1, cost, dp), self.dfs(len(cost) - 2, cost, dp))