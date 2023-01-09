class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = {}
        
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
                
        duplicate, missing = 0, 0
        
        for i in range(1, len(nums) + 1):
            if i in d:
                if d[i] == 2:
                    duplicate = i
            else:
                missing = i
                
        return [duplicate, missing]