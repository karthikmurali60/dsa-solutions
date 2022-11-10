class UnionFind:
    def __init__(self, size: int) -> None:
        self.group = [0] * size
        self.rank = [0] * size
        
        for i in range(size):
            self.group[i] = i
      
    def find(self, node: int) -> int:
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]

    def join(self, node1: int, node2: int) -> bool:
        group1 = self.find(node1)
        group2 = self.find(node2)
        
        # node1 and node2 already belong to same group.
        if group1 == group2:
            return False

        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1

        return True
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pq = []
        n = len(points)
        count, cost = 0, 0
        uf = UnionFind(n)
        
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                manDist = abs(x1 - x2) + abs(y1 - y2)
                
                pq.append([manDist, i, j])
                
        pq.sort()
        
        for dist, p1, p2 in pq:
            if uf.join(p1, p2):
                count += 1
                cost += dist
                
                if count == n - 1:
                    break
            
        return cost
            