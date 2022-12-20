class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        ans = 0
        prefixSums = { 0 : 1 }
        
        for num in nums:
            currSum += num
            
            diff = currSum - k
            
            if diff in prefixSums:
                ans += prefixSums[diff]
                
            if currSum in prefixSums:
                prefixSums[currSum] += 1
            else:
                prefixSums[currSum] = 1
                
        return ans