class Solution:
    def backtrack(self, index, nums, result, ds):
        result.append(list(ds))
        
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
                
            ds.append(nums[i])
            self.backtrack(i + 1, nums, result, ds)
            ds.pop()
            
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        self.backtrack(0, nums, result, [])
        
        return result