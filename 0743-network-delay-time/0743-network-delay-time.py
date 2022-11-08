class Solution:
    def createAdjList(self, times, n):
        adjList = {}
        
        for i in range(1, n + 1):
            adjList[i] = []
            
        for src, tar, time in times:
            adjList[src].append((tar, time))
            
        return adjList
        
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = self.createAdjList(times, n)
        visited = set()
        time = 0
        
        minHeap = [(0, k)]

        while minHeap:
            time1, node1 = heapq.heappop(minHeap)
            if node1 in visited:
                continue
            
            visited.add(node1)
            time = max(time, time1)
            
            for adjNode, adjTime in adjList[node1]:
                if adjNode not in visited:
                    heapq.heappush(minHeap, (time1 + adjTime, adjNode))
            
        return time if len(visited) == n else -1    
        
        