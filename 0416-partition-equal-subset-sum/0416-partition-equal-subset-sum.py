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
        dp = [[False] * (target + 1) for _ in range(len(nums))]
        
        # return self.backtrack(len(nums) - 1, nums, target, dp)
        
        for i in range(len(nums)):
            dp[i][0] = True
            
        if nums[0] <= target:
            dp[0][nums[0]] = True
        
        for index in range(1, len(nums)):
            for targ in range(1, (target + 1), 1):
                notPick = dp[index - 1][targ]
        
                pick = False
                if nums[index] <= target:
                    pick = dp[index - 1][targ - nums[index]]

                dp[index][targ] = pick or notPick
                                
        return dp[len(nums) - 1][target]
    
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        
        arraySum = sum(nums)
        
        if arraySum % 2 != 0:
            return False
        
        return self.subsetSumWithTarget(nums, int(arraySum / 2))
        