class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        patMap = {}
        ans = []
        count = 0
        
        i, j = 0, 0
        k = len(p)
        
        for char in p:
            if char in patMap:
                patMap[char] += 1
            else:
                patMap[char] = 1
        
        count = len(patMap)
        
        while j < len(s):
            if s[j] in patMap:
                patMap[s[j]] -= 1
                if patMap[s[j]] == 0:
                    count -= 1
                    
            if j - i + 1 < k:
                j += 1
            else:
                if count == 0:
                    ans.append(i)
                    
                if s[i] in patMap:
                    patMap[s[i]] += 1
                    if patMap[s[i]] == 1:
                        count += 1
                        
                i += 1
                j += 1
                
        return ans