class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum, maxSum = 0, nums[0]

        for i in nums:
            if(curSum < 0):
                curSum = 0

            curSum += i
            maxSum = max(maxSum, curSum)

        return maxSum
