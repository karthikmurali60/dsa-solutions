#User function Template for python3

class Solution:
    def topoSort(self, V, adj):
        indegree = [0] * V
        
        for i in range(V):
            for node in adj[i]:
                indegree[node] += 1
                
        queue = []
        topo = []
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
                
        while len(queue) != 0:
            ele = queue.pop(0)
            topo.append(ele)
            
            for node in adj[ele]:
                indegree[node] -= 1
                
                if indegree[node] == 0:
                    queue.append(node)
                    
        return topo
    
    def findOrder(self, n, m, prerequisites):
        # Code here
        
        adj = {}
        
        for i in range(n):
            adj[i] = []
        
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            
        topo = self.topoSort(n, adj)
        
        if len(topo) != n:
            return []
        else:
            return topo


#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
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
        n,m = list(map(int, input().strip().split()))
        adj = [[] for i in range(n)]
        prerequisites = []
        
        for i in range(m):
            u,v=map(int,input().split())
            adj[v].append(u)
            prerequisites.append([u,v])
            
        ob = Solution()
        
        res = ob.findOrder(n, m, prerequisites)
        
        if(not len(res)):
            print("No Ordering Possible")
        else:
            if check(adj, n, res):
                print(1)
            else:
                print(0)
# } Driver Code Ends