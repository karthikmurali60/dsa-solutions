class Solution:
    #Function to return list containing vertices in Topological order.
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
            


#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends