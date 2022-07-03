class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        
        for i, number in enumerate(nums):
            if((target - number) in dictionary):
                return [nums.index(target-number), i]
            
            dictionary[number] = i
