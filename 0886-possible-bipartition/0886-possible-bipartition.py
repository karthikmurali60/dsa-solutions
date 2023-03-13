class Solution:
    def isBipartite(self, start, adjList, color):
        queue = [start]
        
        color[start] = 1
        
        while queue:
            ele = queue.pop(0)
            
            for adjNode in adjList[ele]:
                if color[adjNode] == -1:
                    color[adjNode] = not color[ele]
                    queue.append(adjNode)
                    
                elif color[adjNode] == color[ele]:
                    return False
                
        return True
    
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adjList = {}
        
        for i in range(1, n + 1):
            adjList[i] = []
            
        for a, b in dislikes:
            adjList[a].append(b)
            adjList[b].append(a)
            
        color = [-1] * (n + 1)
        
        for i in range(1, n + 1):
            if color[i] == -1:
                if self.isBipartite(i, adjList, color) == False:
                    return False
                
        return True
                
        