class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderMap = { 0 : -1 }
        currSum = 0
        
        for index, num in enumerate(nums):
            currSum += num
            remainder = currSum % k
            
            if remainder not in remainderMap:
                remainderMap[remainder] = index
            elif index - remainderMap[remainder] > 1:
                return True
            
        return False
            
        