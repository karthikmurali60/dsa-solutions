class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        
        if n == 2:
            return 1
        
        third_prev = 0
        second_prev = 1
        first_prev = 1
        
        for i in range(3, n + 1):
            curr = third_prev + second_prev + first_prev
            third_prev = second_prev
            second_prev = first_prev
            first_prev = curr
            
        return first_prev