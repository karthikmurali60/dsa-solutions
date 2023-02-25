class Solution:    
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        count = 0
        
        l, r = 0, len(nums) - 1
        
        upper = pow(10, 9) + 7
        
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                count += pow(2, r - l, upper)
                l += 1
                
        return count % upper