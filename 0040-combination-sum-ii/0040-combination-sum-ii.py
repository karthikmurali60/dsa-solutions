class Solution:
    def backtrack(self, index, candidates, target, result, ds):
        if target == 0:
            result.append(list(ds))
            return
        
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
                
            if candidates[i] > target:
                break
                
            ds.append(candidates[i])
            self.backtrack(i + 1, candidates, target - candidates[i], result, ds)
            ds.pop()
            
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        self.backtrack(0, candidates, target, result, [])
        
        return result