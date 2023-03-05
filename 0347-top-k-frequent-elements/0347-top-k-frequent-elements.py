class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countArr = [[] for _ in range(len(nums) + 1)]
        
        hashMap = {}
        
        for num in nums:
            hashMap[num] = 1 + hashMap.get(num, 0)
            
        for key, val in hashMap.items():
            countArr[val].append(key)
            
        ans = []
                    
        for i in range(len(countArr) - 1, 0, -1):
            for j in range(len(countArr[i])):
                ans.append(countArr[i][j])
                
                if len(ans) == k:
                    return ans