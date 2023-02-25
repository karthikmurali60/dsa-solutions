class Solution:
    def dfs(self, index, candidates, ds, ans, target):
        if index == len(candidates):
            if target == 0:
                ans.append(list(ds))
            return
        
        # pick
        if candidates[index] <= target:
            ds.append(candidates[index])
            self.dfs(index, candidates, ds, ans, target - candidates[index])
            ds.pop()
            
        # not pick
        self.dfs(index + 1, candidates, ds, ans, target)
  
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        self.dfs(0, candidates, [], ans, target)
        
        return ans