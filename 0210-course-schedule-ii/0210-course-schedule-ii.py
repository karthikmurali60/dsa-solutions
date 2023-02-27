class Solution:
    def topoSort(self, n, adj):
        indegree = [0] * n
        
        for i in range(n):
            for node in adj[i]:
                indegree[node] += 1
                
        queue = []
        topo = []
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        while len(queue) != 0:
            ele = queue.pop(0)
            topo.append(ele)
            
            for node in adj[ele]:
                indegree[node] -= 1
                
                if indegree[node] == 0:
                    queue.append(node)
                    
        return topo
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        
        for i in range(numCourses):
            adj[i] = []
            
        for course, prereq in prerequisites:
            adj[prereq].append(course)
                        
        topo = self.topoSort(numCourses, adj)
                
        if len(topo) != numCourses:
            return []
        else:
            return topo
            