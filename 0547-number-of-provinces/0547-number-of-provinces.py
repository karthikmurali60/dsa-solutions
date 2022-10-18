class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            visited.add(i)
            
            for j in range(len(isConnected)):
                if isConnected[i][j] and j not in visited:
                    dfs(j)
            
        numberOfProvinces = 0
        visited = set()
        
        for i in range(len(isConnected)):
            if i not in visited:
                numberOfProvinces += 1
                dfs(i)
                
        return numberOfProvinces