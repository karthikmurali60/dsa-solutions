class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        max_val = max(nums)
        
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        taken = []
        
        moves = 0
        for x in range(len(nums) + max_val):
            if x in count and count[x] >= 2:
                taken.extend([x] * (count[x] - 1))
            elif taken and x not in count:
                moves += x - taken.pop()
                
        return moves