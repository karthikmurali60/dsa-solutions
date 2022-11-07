class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        adjList = {}
        
        for i in range(n):
            adjList[i] = []
            
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                distance = abs(x1 - x2) + abs(y1 - y2)
                
                adjList[i].append([distance, j])
                adjList[j].append([distance, i])
                
        
        visited = set()
        minHeap = [[0,0]]
        res = 0
        
        while len(visited) < n:
            cost, i = heapq.heappop(minHeap)
            
            if i in visited:
                continue
            
            res += cost
            visited.add(i)
            
            for cost, adj in adjList[i]:
                if adj not in visited:
                    heapq.heappush(minHeap, [cost, adj])
        
        return res