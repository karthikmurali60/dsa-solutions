class Solution:
    def backtrack(self, nums, result, vis, ds):
        if len(ds) == len(nums):
            result.append(list(ds))
            return
        
        for i in range(0, len(nums)):
            if not vis[i]:
                vis[i] = 1
                ds.append(nums[i])
                self.backtrack(nums, result, vis, ds)
                ds.pop()
                vis[i] = 0
        
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        vis = [0] * len(nums)

        self.backtrack(nums, result, vis, [])
        
        return result