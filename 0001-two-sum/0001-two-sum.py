class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for idx, num in enumerate(nums):
            if target - num in numsDict:
                return [idx, numsDict[target - num]]
            
            numsDict[num] = idx
    