class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hashMap = {}
        
        for char in s:
            if char in hashMap:
                return char
            
            hashMap[char] = 1
            