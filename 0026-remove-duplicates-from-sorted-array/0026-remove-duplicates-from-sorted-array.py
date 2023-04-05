class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        
        left, right = 0, 1
        k = 1
        
        while right < len(nums):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
                k += 1
            
            right += 1
        
        return k
            