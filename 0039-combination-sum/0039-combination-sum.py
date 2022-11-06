class Solution:
    def backtrack(self, index, candidates, target, result, temp):
        if index == len(candidates):
            if target == 0:
                result.append(list(temp))
            
            return
        
        if target >= candidates[index]:
            temp.append(candidates[index])
            self.backtrack(index, candidates, target - candidates[index], result, temp)
            temp.pop()
            
        self.backtrack(index + 1, candidates, target, result, temp)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        self.backtrack(0, candidates, target, result, [])
        
        return result