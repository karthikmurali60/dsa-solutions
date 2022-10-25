class Solution:
    def backtrack(self, index, nums, dp):
        if index == 0:
            return nums[index]
        if index < 0:
            return 0
        if dp[index] != -1:
            return dp[index]
        
        pick = nums[index] + self.backtrack(index - 2, nums, dp)
        notPick = self.backtrack(index - 1, nums, dp)
        
        dp[index] = max(pick, notPick)
        
        return max(pick, notPick)
    
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        return self.backtrack(len(nums) - 1, nums, dp)