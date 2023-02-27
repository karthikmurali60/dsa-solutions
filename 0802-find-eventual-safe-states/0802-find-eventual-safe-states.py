class Solution:
    def dfs(self, index, graph, vis):
        vis[index] = 2
        
        for node in graph[index]:
            if vis[node] == 0:
                if self.dfs(node, graph, vis):
                    return True
            elif vis[node] == 2:
                return True
            
        vis[index] = 1
        return False    
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        vis = [0] * len(graph)
        
        ans = []
        
        for i in range(len(graph)):
            if vis[i] == 0:
                self.dfs(i, graph, vis)
                
        for i in range(len(vis)):
            if vis[i] == 1:
                ans.append(i)
        
        ans.sort()
        
        return ans