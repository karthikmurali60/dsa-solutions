class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = {}
        n = len(nums)

        freqArr = [[] for i in range(n + 1)]
        
        for i in range(n):
            if nums[i] in numsDict:
                numsDict[nums[i]] += 1
            else:
                numsDict[nums[i]] = 1
                
        for key, val in numsDict.items():
            freqArr[val].append(key)
            
        result = []
                
        for i in range(len(freqArr) - 1, 0, -1):
            for j in freqArr[i]:
                result.append(j)
                k -= 1
                
                if k == 0:
                    return result
        