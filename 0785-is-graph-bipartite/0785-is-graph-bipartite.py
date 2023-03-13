class Solution:
    def checkBipartite(self, node, graph, color):
        color[node] = 0
        
        queue = [node]
        
        while queue:
            ele = queue.pop(0)
        
            for adjNode in graph[ele]:
                if color[adjNode] == -1:
                    color[adjNode] = not color[ele]
                    queue.append(adjNode)
                    
                elif color[adjNode] == color[ele]:
                    return False
                
        return True
                
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)
                
        for i in range(len(graph)):
            if color[i] == -1:
                if self.checkBipartite(i, graph, color) == False:
                    return False
                
        return True