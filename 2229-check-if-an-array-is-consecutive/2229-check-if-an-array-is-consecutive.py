class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        minNumber = float('inf')
        numSet = set()
        
        for num in nums:
            minNumber = min(minNumber, num)
            numSet.add(num)
            
        start, end = minNumber, (minNumber + len(nums))
                
        for i in range(start, end):
            if i not in numSet:
                return False
            
        return True