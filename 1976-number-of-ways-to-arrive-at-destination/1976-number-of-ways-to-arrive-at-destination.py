class Solution:
    def createAdjList(self, n, roads):
        adjList = {}
        
        for i in range(n):
            adjList[i] = []
            
        for src, dst, time in roads:
            adjList[src].append((time, dst))
            adjList[dst].append((time, src))
            
        return adjList
        
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adjList = self.createAdjList(n, roads)
        ways = [0] * n
        time = [float('inf')] * n
        
        # Number of ways to reach starting node is 1 and the time is 0.         
        ways[0] = 1
        time[0] = 0
        
        minHeap = [(0, 0)]
        
        while minHeap:
            time1, node1 = heapq.heappop(minHeap)
            
            for adjTime, adjNode in adjList[node1]:
                if time1 + adjTime < time[adjNode]:
                    time[adjNode] = time1 + adjTime
                    ways[adjNode] = ways[node1]
                    heapq.heappush(minHeap, (time[adjNode], adjNode))
                elif time1 + adjTime == time[adjNode]:
                    ways[adjNode] += ways[node1]
        
        return ((ways[n-1]) % (pow(10, 9) + 7))