class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        
        for index, num in enumerate(nums):
            if target - num in numsDict:
                return [index, numsDict[target - num]]
            
            numsDict[num] = index