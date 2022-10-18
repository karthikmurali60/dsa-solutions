class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        scores = [0] * (n + 1)
        
        if len(trust) < n-1:
            return -1
        if len(trust) == 0 and n == 1:
            return 1
        
        for a,b in trust:
            scores[a] -= 1
            scores[b] += 1
            
        for i in range(n + 1):
            if scores[i] == n-1:
                return i
        
        return -1