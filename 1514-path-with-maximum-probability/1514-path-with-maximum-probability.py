class Solution:
    def createAdjList(self, n, edges, succProb):
        adjList = {}
        for i in range(n):
            adjList[i] = []
            
        for i in range(len(edges)):
            src, des = edges[i]
            probability = -1 * succProb[i]
            adjList[src].append((probability, des))
            adjList[des].append((probability, src))
            
        return adjList
    
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adjList = self.createAdjList(n, edges, succProb)
        minHeap = [(-1, start)]
        probability = -float('inf')
        currProb = 1
        visited = set()
                
        while minHeap:
            prob, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            visited.add(node)
            currProb = -1 * prob
            if node == end:
                probability = max(probability, currProb)
            
            for adjProb, adjNode in adjList[node]:
                if adjNode not in visited:
                    heapq.heappush(minHeap, (-1 * adjProb * prob, adjNode))
                    
        return probability if end in visited else 0
