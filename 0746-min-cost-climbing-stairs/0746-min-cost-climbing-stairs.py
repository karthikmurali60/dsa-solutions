class Solution:
    def backtrack(self, index, cost, dp):
        if index < 0:
            return float('inf')
        
        if index == 0 or index == 1:
            return cost[index]
        
        if dp[index] != -1:
            return dp[index]
        
        dp[index] = cost[index] + min(self.backtrack(index - 1, cost, dp), self.backtrack(index - 2, cost, dp))
        
        return dp[index]
        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * (len(cost) + 1)
        
        return min(self.backtrack(len(cost) - 2, cost, dp), self.backtrack(len(cost) - 1, cost, dp))
          