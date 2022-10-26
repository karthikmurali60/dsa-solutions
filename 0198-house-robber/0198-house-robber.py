class Solution:
#     def backtrack(self, index, nums, dp):
#         if index == 0:
#             return nums[index]
#         if index < 0:
#             return 0
#         if dp[index] != -1:
#             return dp[index]
        
#         pick = nums[index] + self.backtrack(index - 2, nums, dp)
#         notPick = self.backtrack(index - 1, nums, dp)
        
#         dp[index] = max(pick, notPick)
        
#         return max(pick, notPick)
    
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
        
        