class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            pick = nums[i]
            if i > 1:
                pick += dp[i - 2]
                
            notPick = dp[i - 1]
            
            dp[i] = max(pick, notPick)
            
        return dp[len(nums) - 1]