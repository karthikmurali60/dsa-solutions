class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currCount, maxCount = 0, -1e9
        
        for num in nums:
            if num == 1:
                currCount += 1
            else:
                maxCount = max(maxCount, currCount)
                currCount = 0
        
        maxCount = max(maxCount, currCount)
        
        return maxCount
