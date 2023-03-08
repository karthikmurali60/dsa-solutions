class Solution:
    def removeVowels(self, s: str) -> str:
        l = list(s)
        
        i = 0
        while i < len(l):
            if l[i] in ['a', 'e', 'i', 'o', 'u']:
                l.pop(i)
                continue
                
            i += 1
                
        return ''.join(l)