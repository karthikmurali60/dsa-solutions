class Solution:
    def isCycle(self, node, prevNode, adjList, vis):        
        vis.add(node)
        
        for adjNode in adjList[node]:
            if adjNode != prevNode and adjNode in vis:
                return True
            if adjNode == prevNode:
                continue
            if self.isCycle(adjNode, node, adjList, vis):
                return True
            
        return False
        
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {}
        
        for i in range(n):
            adjList[i] = []
        
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
            
        vis = set()
        
        # If there is a cycle, then graph is not a valid tree
        if self.isCycle(0, -1, adjList, vis):
            return False
        
        # After DFS, if all the nodes are not visited, then there are
        # multiple components in the graph and hence it is not a valid tree
        if len(vis) != n:
            return False
        
        return True
