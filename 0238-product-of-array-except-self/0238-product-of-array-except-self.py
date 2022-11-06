class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        result = []
        result.append(1)
        
        prefix = 1
        for i in range(1, n):
            result.append(nums[i - 1] * prefix)
            prefix *= nums[i - 1]
                
        postfix = 1
        for i in range(len(result) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
            
        return result
            
        