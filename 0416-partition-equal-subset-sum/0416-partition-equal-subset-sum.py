class Solution:
    def backtrack(self, index, nums, target, dp):
        if target == 0:
            return True
        
        if index == 0:
            return nums[index] == target
        
        if dp[index][target] != -1:
            return dp[index][target]
        
        notPick = self.backtrack(index - 1, nums, target, dp)
        
        pick = False
        if nums[index] <= target:
            pick = self.backtrack(index - 1, nums, target - nums[index], dp)
            
        dp[index][target] = pick or notPick
            
        return pick or notPick
    
    def subsetSumWithTarget(self, nums, target):
        dp = [[-1] * (target + 1) for _ in range(len(nums) + 1)]
        
        return self.backtrack(len(nums) - 1, nums, target, dp)
    
    def canPartition(self, nums: List[int]) -> bool:
        arraySum = sum(nums)
        
        if arraySum % 2 != 0:
            return False
        
        return self.subsetSumWithTarget(nums, int(arraySum / 2))
        