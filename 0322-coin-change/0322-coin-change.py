class Solution:
    def backtrack(self, index, coins, amount, dp):
        if index == 0:
            if amount % coins[0] == 0:
                return int(amount / coins[index])
            else:
                return float('inf')
            
        if dp[index][amount] != -1:
            return dp[index][amount]
            
        notPick = 0 + self.backtrack(index - 1, coins, amount, dp)
        
        pick = float('inf')
        if coins[index] <= amount:
            pick = 1 + self.backtrack(index, coins, amount - coins[index], dp)
            
        dp[index][amount] = min(pick, notPick)
            
        return min(pick, notPick)
               
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        if len(coins) == 1:
            if amount % coins[0] == 0:
                return int(amount / coins[0])
            else:
                return -1
        
        
        dp = [[-1] * (amount + 1) for i in range(len(coins))]
        
        ans = self.backtrack(len(coins) - 1, coins, amount, dp)
        
        if ans == float('inf'):
            return -1
        else:
            return ans
        