class Solution:
    def createAdjList(self, n, edges):
        adjList = {}
        
        for i in range(n):
            adjList[i] = []
            
        for start, end in edges:
            adjList[start].append(end)
            adjList[end].append(start)
            
        return adjList
    
    def find_circle(self, node, parent, circle, visited, adjList):
            if node in visited:
                return (True, node)
            
            for adjNode in adjList[node]:
                if adjNode == parent: 
                    continue
                    
                visited.add(node)
                circle.append(node)
                
                status, res = self.find_circle(adjNode, node, circle, visited, adjList)
                if status: 
                    return status, res
                
                circle.pop()
                visited.remove(node)

            return False, None
        
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = self.createAdjList(n, edges)
        
        circle = []
        visited = set()
        
        _, node = self.find_circle(0, None, circle, visited, adjList)
        circle = circle[circle.index(node):] 

        result = [0] * n        
        visited = set(circle)

        steps = 0
        while circle:
            queue = []
            steps += 1
            
            for x in circle:
                for adjNode in adjList[x]:
                    if adjNode in visited:
                        continue
                        
                    result[adjNode] = steps
                    visited.add(adjNode)
                    queue.append(adjNode)
                    
            circle = queue
            
        return result        