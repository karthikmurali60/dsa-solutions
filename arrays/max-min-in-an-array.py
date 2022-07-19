class Solution:
    def findSum(self,A):
        minEle, maxEle = 1000000000, -1000000000

        for i in A:
            minEle = min(minEle, i)
            maxEle = max(maxEle, i)

        return (minEle + maxEle)
