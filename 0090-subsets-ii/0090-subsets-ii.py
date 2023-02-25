class Solution:
    def dfs(self, index, nums, ds, ans):
        ans.append(list(ds))
        
        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]:
                continue
                
            ds.append(nums[i])
            self.dfs(i + 1, nums, ds, ans)
            ds.pop()
    
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        nums.sort()
        
        self.dfs(0, nums, [], ans)
        
        return ans