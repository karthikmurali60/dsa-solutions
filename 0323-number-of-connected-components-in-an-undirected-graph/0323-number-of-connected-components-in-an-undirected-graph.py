class Solution:
    def convertToAdjList(self, n, edges):
        adjList = {}
        
        for i in range(n):
            adjList[i] = []
        
        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
            
        return adjList
        
    def dfs(self, vis, adjList, src):
        vis[src] = 1
        
        for i in adjList[src]:
            if not vis[i]:
                self.dfs(vis, adjList, i)
        
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = self.convertToAdjList(n, edges)
        vis = [0] * n
        count = 0
        
        for i in range(n):
            if not vis[i]:
                count += 1
                self.dfs(vis, adjList, i)
        
        return count