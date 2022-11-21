class Solution:
    def backtrack(self, index, nums, result, ds):
        if index == len(nums):
            result.append(list(ds))
            return
        
        # pick the element at the current index.
        ds.append(nums[index])
        self.backtrack(index + 1, nums, result, ds)
        ds.pop()
        
        # do not pick the element at the current index.
        self.backtrack(index + 1, nums, result, ds)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        self.backtrack(0, nums, result, [])
        
        return result