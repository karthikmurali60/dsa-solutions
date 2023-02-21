#User function Template for python3


class Solution:
    def dfs(self, index, adj, vis, pathVis):
        vis[index] = 1
        pathVis[index] = 1
        
        for node in adj[index]:
            # recursively visit all the adj nodes if not visited.
            if not vis[node]:
                if self.dfs(node, adj, vis, pathVis):
                    return True
            # if visited and also in the same path, then there is a cycle.
            elif pathVis[node]:
                return True
        
        # There was no cycle on this path. Hence mark all the nodes visited in
        # this path to 0 and return False.
        pathVis[index] = 0
        return False
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        
        vis = [0] * V
        pathVis = [0] * V
        
        for i in range(V):
            if not vis[i]:
                if self.dfs(i, adj, vis, pathVis):
                    return True
                    
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends