class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:        
        costsSum = sum(costs)
        
        if costsSum <= coins:
            return len(costs)
        
        costs.sort()
        
        if costs[0] > coins:
            return 0
        
        maxCount, currCost = 0, 0

        for cost in costs:
            if currCost + cost <= coins:
                maxCount += 1
                currCost += cost
        
        return maxCount