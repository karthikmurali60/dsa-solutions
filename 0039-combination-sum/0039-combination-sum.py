class Solution:
    def backtrack(self, index, candidates, target, result, ds):
        if index == len(candidates):
            if target == 0:
                result.append(list(ds))
            
            return
        
        # pick the element at the current index.
        if target >= candidates[index]:
            ds.append(candidates[index])
            self.backtrack(index, candidates, target - candidates[index], result, ds)
            ds.pop()
        
        # do not pick the element at the current index.
        self.backtrack(index + 1, candidates, target, result, ds)
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        self.backtrack(0, candidates, target, result, [])
        
        return result