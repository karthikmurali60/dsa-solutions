class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        result = 0
        i, j = 0, len(nums) - 1
        upper = 10 ** 9 + 7
        
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                result += pow(2, j - i, upper)
                i += 1
                
        return result % upper