class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        hashMap = {}
        
        for i in range(len(nums) - 1):
            currSum = nums[i] + nums[i + 1]
            
            if currSum in hashMap:
                return True
            
            hashMap[currSum] = 1
            
        return False
            