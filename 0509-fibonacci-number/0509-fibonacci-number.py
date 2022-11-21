class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        prevv = 0
        prev = 1
        
        for i in range(2, n+1):
            curr = prevv + prev
            prevv = prev
            prev = curr
            
        return prev
        