class Solution:
    def toLowerCase(self, s: str) -> str:        
        l = list(s)
        
        for idx, char in enumerate(l):
            if ord(char) >= 65 and ord(char) <= 90:
                l[idx] = chr(ord(char) + 32)
                
        return ''.join(l)