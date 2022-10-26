class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        
        for i in range(1, len(nums)):
            pick = nums[i] 
            if i > 1:
                pick += dp[i - 2]
                
            notPick = dp[i - 1]
            
            dp[i] = max(pick, notPick)
            
        return dp[len(nums) - 1]
        
        