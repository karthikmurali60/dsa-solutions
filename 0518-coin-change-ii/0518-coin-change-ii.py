class Solution:
    def backtrack(self, index, amount, coins, dp):
        if index == 0:
            if amount % coins[0] == 0:
                return 1
            else:
                return 0
            
        if dp[index][amount] != -1:
            return dp[index][amount]
            
        notPick = self.backtrack(index - 1, amount, coins, dp)
        
        pick = 0
        if coins[index] <= amount:
            pick = self.backtrack(index, amount - coins[index], coins, dp)
            
        dp[index][amount] = pick + notPick
            
        return pick + notPick
                
    
    
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount + 1) for i in range(len(coins))]
        
        return self.backtrack(len(coins) - 1, amount, coins, dp)        
        