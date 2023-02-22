class Solution:
    def base(self, nums):
        n = len(nums)
        
        dp = [-1] * n
        
        dp[0] = nums[0]
        
        for i in range(1, n):
            pick = nums[i]
            if i > 1:
                pick += dp[i - 2]
                
            notPick = 0 + dp[i - 1]
            
            dp[i] = max(pick, notPick)
        
        return dp[n - 1]
        
    def rob(self, nums: List[int]) -> int:
        # First and last house are adjacent. Hence in any solution, they both cannot be present
        # together. Its either of them.
        
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        array1 = nums[ : n - 1]
        array2 = nums[1 : ]
        
        return max(self.base(array1), self.base(array2))