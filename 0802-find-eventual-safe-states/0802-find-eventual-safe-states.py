class Solution:
#     def dfs(self, index, graph, vis):
#         vis[index] = 2
        
#         for node in graph[index]:
#             if vis[node] == 0:
#                 if self.dfs(node, graph, vis):
#                     return True
#             elif vis[node] == 2:
#                 return True
            
#         vis[index] = 1
#         return False    
    
#     def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
#         vis = [0] * len(graph)
        
#         ans = []
        
#         for i in range(len(graph)):
#             if vis[i] == 0:
#                 self.dfs(i, graph, vis)
                
#         for i in range(len(vis)):
#             if vis[i] == 1:
#                 ans.append(i)
        
#         ans.sort()
        
#         return ans

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        revGraph = {}
        
        for i in range(len(graph)):
            revGraph[i] = []
            
        for node, neighbours in enumerate(graph):
            for neighbour in neighbours:
                revGraph[neighbour].append(node)
                
        indegree = [0] * len(graph)
        
        for node, neighbours in revGraph.items():
            for neighbour in neighbours:
                indegree[neighbour] += 1
                
        queue = []
        
        for i in range(len(graph)):
            if indegree[i] == 0:
                queue.append(i)
                
        safe = []
        while queue:
            ele = queue.pop(0)
            
            safe.append(ele)
            
            for adjNode in revGraph[ele]:
                indegree[adjNode] -= 1
                
                if indegree[adjNode] == 0:
                    queue.append(adjNode)
                    
        safe.sort()
        
        return safe
        