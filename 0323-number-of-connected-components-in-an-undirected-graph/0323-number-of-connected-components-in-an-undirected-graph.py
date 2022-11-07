class Solution:
    def convertEdgesToAdjMatrix(self, edges, n):
        adjMatrix = {}
  
        for i in range(n):
            adjMatrix[i] = []

        for a, b in edges:
            adjMatrix[a].append(b)
            adjMatrix[b].append(a)
            
        return adjMatrix
    
    def dfs(self, index, edges, visited, adjMatrix):
        visited[index] = 1
        
        for node in adjMatrix[index]:
            if not visited[node]:
                self.dfs(node, edges, visited, adjMatrix)
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        
        adjMatrix = self.convertEdgesToAdjMatrix(edges, n)
        visited = [0] * n
        
        for i in range(n):
            if not visited[i]:
                components += 1
                self.dfs(i, edges, visited, adjMatrix)
                
        return components
        