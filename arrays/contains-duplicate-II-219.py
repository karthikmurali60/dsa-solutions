class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_occurence = {}
        
        for i, num in enumerate(nums):
            if(num in last_occurence and i - last_occurence[num] <= k):
                return True
            
            last_occurence[num] = i
        
        return False
