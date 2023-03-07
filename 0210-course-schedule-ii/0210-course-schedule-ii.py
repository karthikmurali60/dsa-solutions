class Solution:
    def topoSort(self, prerequisites, numCourses, adjList):
        indegree = [0] * numCourses
        
        for neighbours in adjList.values():
            for course in neighbours:
                indegree[course] += 1
                
        queue = []
        topo = []
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                
        while queue:
            ele = queue.pop(0)
            
            topo.append(ele)
            
            for node in adjList[ele]:
                indegree[node] -= 1
                
                if indegree[node] == 0:
                    queue.append(node)
        
        return topo
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {}
        
        for i in range(numCourses):
            adjList[i] = []
            
        for course, prereq in prerequisites:
            adjList[prereq].append(course)
            
        topo = self.topoSort(prerequisites, numCourses, adjList)
        
        if len(topo) != numCourses:
            return []
        
        return topo