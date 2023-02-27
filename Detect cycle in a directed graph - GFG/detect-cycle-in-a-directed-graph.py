#User function Template for python3


class Solution:
    def topoSort(self, V, adj):
        indegree = [0] * V
        
        queue = []
        
        topo = []
        
        for i in range(V):
            for node in adj[i]:
                indegree[node] += 1
        
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
                
        while len(queue) != 0:
            ele = queue.pop(0)
            
            for node in adj[ele]:
                indegree[node] -= 1
                
                if indegree[node] == 0:
                    queue.append(node)
                    
            topo.append(ele)
            
        return topo

    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        topo = self.topoSort(V, adj)
        
        if len(topo) != V:
            return True
        else:
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