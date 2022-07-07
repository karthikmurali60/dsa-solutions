# In the binary representation, the least significant 1-bit in n
# always corresponds to a 0-bit in n - 1. Therefore, ANDing the
# two numbers n and n - 1 always flips the least significant 1-bit
# in n to 0, and keeps all other bits the same.
class Solution:
    def numberOf1Bits(self, n: int) -> int:
        count = 0

        while(n != 0):
            count += 1
            n &= n-1

        return count
