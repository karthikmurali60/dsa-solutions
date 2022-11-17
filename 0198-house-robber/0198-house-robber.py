class Solution:
    def backtrack(self, nums, index, dp):
        if index == 0:
            return nums[index]
        
        if index < 0:
            return 0
        
        if dp[index] != -1:
            return dp[index]
        
        pick = nums[index] + self.backtrack(nums, index - 2, dp)
        notPick = self.backtrack(nums, index - 1, dp)
        
        dp[index] = max(pick, notPick)
        
        return max(pick, notPick)
    
    
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        
        return self.backtrack(nums, len(nums) - 1, dp)