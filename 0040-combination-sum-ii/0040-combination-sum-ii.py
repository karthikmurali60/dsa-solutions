class Solution:
    def dfs(self, index, candidates, ds, ans, target):
        if target == 0 and list(ds) not in ans:
            ans.append(list(ds))
            return
        
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
                
            if candidates[i] > target:
                break
                
            ds.append(candidates[i])
            self.dfs(i + 1, candidates, ds, ans, target - candidates[i])
            ds.pop()
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        candidates.sort()
        
        self.dfs(0, candidates, [], ans, target)
        
        return ans