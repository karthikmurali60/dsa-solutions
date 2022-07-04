class Solution:
    def bestTime(self, prices: List[int]) -> int:
        left, right, maxProfit = 0, 1, 0

        while(right < len(prices)):
            if(prices[left] < prices[right]):
                maxProfit = max(maxProfit, (nums[right] - nums[left]))
            else:
                left = right
            
            right += 1
        
        return maxProfit
