class Solution:
    def dfs(self, index, graph, result, ds, n):
        if index == n-1:
            ds.append(index)
            result.append(list(ds))
            return
        
        ds.append(index)
        for node in graph[index]:
            self.dfs(node, graph, result, ds, n)
            ds.pop()
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        
        self.dfs(0, graph, result, [], len(graph))
        
        return result