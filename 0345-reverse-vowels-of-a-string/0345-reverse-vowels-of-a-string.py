class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        
        for char in s:
            if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                vowels.append(char)
                
        result = []
        
        for char in s:
            if char in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                result.append(vowels.pop())
            else:
                result.append(char)
                
        return ''.join(result)