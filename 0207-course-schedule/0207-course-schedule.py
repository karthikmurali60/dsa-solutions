class Solution:
    def dfs(self, index, adj, vis):
        vis[index] = 2
        
        for node in adj[index]:
            if vis[node] == 0:
                if self.dfs(node, adj, vis):
                    return True
            elif vis[node] == 2:
                return True
            
        vis[index] = 1
        return False
    
    def detectCycle(self, n, adj):
        vis = [0] * n
        
        for i in range(n):
            if vis[i] == 0:
                if self.dfs(i, adj, vis):
                    return True
        
        return False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        adj = {}
        
        for i in range(numCourses):
            adj[i] = []
            
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            
        return not self.detectCycle(numCourses, adj)