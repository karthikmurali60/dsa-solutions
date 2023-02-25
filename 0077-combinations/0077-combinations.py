class Solution:
    def dfs(self, index, nums, ds, ans, k):
        if len(ds) == k:
            ans.append(list(ds))
            return
            
        if index == len(nums):
            if len(ds) == k:
                ans.append(list(ds))
            return
        
        # pick
        ds.append(nums[index])
        self.dfs(index + 1, nums, ds, ans, k)
        ds.pop()
        
        # not pick
        self.dfs(index + 1, nums, ds, ans, k)
    
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        nums = [i for i in range(1, n + 1)]
        
        self.dfs(0, nums, [], ans, k)
        
        return ans