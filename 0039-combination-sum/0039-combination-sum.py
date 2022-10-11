class Solution:
    def findCombination(self, index, candidates, target, ans, ds):
        if index == len(candidates):
            if target == 0:
                ans.append(list(ds))
            return
        
        if candidates[index] <= target:
            ds.append(candidates[index])
            self.findCombination(index, candidates, target - candidates[index], ans, ds)
            ds.pop()
        
        self.findCombination(index + 1, candidates, target, ans, ds)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        self.findCombination(0, candidates, target, ans, [])
        
        return ans