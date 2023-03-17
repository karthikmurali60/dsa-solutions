class Solution:
    def atmost(self, nums, k):
        left, right = 0, 0
        count = 0
        numsMap = {}
        
        while right < len(nums):
            numsMap[nums[right]] = 1 + numsMap.get(nums[right], 0)
            
            while len(numsMap) > k:
                numsMap[nums[left]] -= 1
                
                if numsMap[nums[left]] == 0:
                    del numsMap[nums[left]]
                    
                left += 1
                
            count += right - left + 1
            
            right += 1
            
        return count
    
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmost(nums, k) - self.atmost(nums, k - 1)