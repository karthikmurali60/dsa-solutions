class Solution:
    def dfs(self, house, lastColor, m, n, costs, dp):
        if house == 0:
            minCost = float('inf')
            
            for i in range(n):
                if i != lastColor:
                    minCost = min(minCost, costs[house][i])
                    
            return minCost
        
        if dp[house][lastColor] != -1:
            return dp[house][lastColor]
        
        minCost = float('inf')
        
        for i in range(n):
            if i != lastColor:
                currCost = costs[house][i] + self.dfs(house - 1, i, m, n, costs, dp)
                minCost = min(minCost, currCost)
                
        dp[house][lastColor] = minCost
        
        return minCost
                
    def minCostII(self, costs: List[List[int]]) -> int:
        m, n = len(costs), len(costs[0])
        
        dp = [[-1] * (n + 1) for _ in range(m)]
        
        return self.dfs(m - 1, n, m, n, costs, dp)