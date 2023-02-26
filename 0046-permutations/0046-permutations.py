class Solution:
    def dfs(self, index, nums, ds, ans, vis):
        if index == len(nums):
            ans.append(list(ds))
            return
        
        for i in range(len(nums)):
            if not vis[i]:
                vis[i] = 1
                ds.append(nums[i])
                self.dfs(index + 1, nums, ds, ans, vis)
                vis[i] = 0
                ds.pop()
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        vis = [0] * len(nums)
        
        self.dfs(0, nums, [], ans, vis)
        
        return ans