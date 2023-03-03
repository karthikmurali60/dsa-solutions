class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = {}
        
        for num in nums:
            if num in h:
                return True
            
            h[num] = 1
        
        return False