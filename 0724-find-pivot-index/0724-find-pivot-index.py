class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arraySum = sum(nums)
        currSum = 0
        
        for index in range(len(nums)):
            if currSum == arraySum - nums[index] - currSum:
                return index
            
            currSum += nums[index]
            
        return -1