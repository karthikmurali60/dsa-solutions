from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def dfs(self, source, parent, adj, vis):
        vis[source] = 1

        for node in adj[source]:
            if vis[node] and node != parent:
                return True
            if not vis[node]:
                if self.dfs(node, source, adj, vis):
                    return True

	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
		vis = [0] * (V)
		
		for i in range(V):
		    if not vis[i]:
		        if self.dfs(i, -1, adj, vis):
		            return True
		   
		return False


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends