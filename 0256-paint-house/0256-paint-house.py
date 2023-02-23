class Solution:
    def dfs(self, day, lastTask, m, n, costs, dp):
        if day == 0:
            minCost = float('inf')
            
            for i in range(n):
                if i != lastTask:
                    minCost = min(minCost, costs[day][i])
                    
            return minCost
        
        if dp[day][lastTask] != -1:
            return dp[day][lastTask]
        
        minCost = float('inf')
        
        for i in range(n):
            if i != lastTask:
                cost = costs[day][i] + self.dfs(day - 1, i, m, n, costs, dp)
                minCost = min(minCost, cost)
                
        dp[day][lastTask] = minCost
        
        return minCost
    
    def minCost(self, costs: List[List[int]]) -> int:
        m, n = len(costs), len(costs[0])
        
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        
        return self.dfs(m - 1, n, m, n, costs, dp)