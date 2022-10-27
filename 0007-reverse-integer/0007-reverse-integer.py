class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        negative = True if x < 0 else False
        
        x = abs(x)
        
        while x > 0:
            digit = x % 10
            reverse = (reverse * 10) + digit
            x = x // 10
            
        reverse = (-1 * reverse) if negative else reverse
        
        if reverse >= (pow(2, 31) - 1) or reverse <= (-1 * pow(2, 31)):
            return 0
            
        return reverse