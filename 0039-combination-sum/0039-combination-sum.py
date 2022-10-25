class Solution:
    def dfs(self, index, candidates, result, ds, target):
        if index == len(candidates):
            if target == 0:
                result.append(list(ds))
            return
        
        # pick the element at the current index
        if candidates[index] <= target:
            ds.append(candidates[index])
            self.dfs(index, candidates, result, ds, target - candidates[index])
            ds.pop()
        
        # do not pick the element at the current index
        self.dfs(index + 1, candidates, result, ds, target)
        
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        self.dfs(0, candidates, result, [], target)
        
        return result