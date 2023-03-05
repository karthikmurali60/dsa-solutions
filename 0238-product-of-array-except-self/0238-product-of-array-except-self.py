class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix, ans = [1] * len(nums), [1] * len(nums), []
        
        currProduct = 1
        for i in range(1, len(nums)):
            currProduct *= nums[i - 1]
            prefix[i] = currProduct
            
        currProduct = 1
        for i in range(len(nums) - 2, -1, -1):
            currProduct *= nums[i + 1]
            postfix[i] = currProduct
            
        for i in range(len(nums)):
            ans.append(prefix[i] * postfix[i])
            
        return ans