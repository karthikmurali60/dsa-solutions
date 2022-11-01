class Solution:
    def matching(self, s1, s2):
        print(s1, s2)
        n = len(s1)
        
        for i in range(n):
            if s1[i] != s2[i]:
                return False
            
        return True
        
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        h = len(haystack)
        
        if h == n:
            return 0 if self.matching(haystack, needle) else -1
        
        for i in range(0, h - n + 1):
            if self.matching(haystack[i:i+n], needle):
                return i
        
        return -1
                