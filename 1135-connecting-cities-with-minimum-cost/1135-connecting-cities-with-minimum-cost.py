class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size + 1)]
        self.rank = [1] * (size + 1)

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        # To connect n cities with minimum cost, there has to be ATLEAST
        # n - 1 connections.
        if len(connections) < n - 1:
            return -1
        
        pq = []
        cost, count = 0, 0

        for src, des, weight in connections:
            heapq.heappush(pq, (weight, src, des))    
                
        uf = UnionFind(n)
        
        while pq and count != n - 1:
            weight, des, src = heapq.heappop(pq)
            
            if uf.connected(src, des):
                continue
                
            cost += weight
            uf.union(src, des)
            count += 1
            
        return cost
        