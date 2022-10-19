

from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def find(self, V, adj, src, visited):
		visited[src] = 1
		
		queue = [[src, -1]]
		
		while queue:
		    ele, parent = queue.pop(0)
		    
		    for i in adj[ele]:
		        if i != parent and visited[i]:
		            return True
		            
		        if i != parent:
		            queue.append([i, ele])
                    visited[i] = 1
		        
		return False
    
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		visited = [0] * V
		
		for i in range(V):
		    if self.find(V, adj, i, visited[:]):
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