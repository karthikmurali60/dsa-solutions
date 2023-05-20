#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        
        queue = [0]
        
        result = []
        
        vis = [0] * V
        vis[0] = 1
        
        while queue:
            node = queue.pop(0)
            result.append(node)
            
            for adjNode in adj[node]:
                if not vis[adjNode]:
                    vis[adjNode] = 1
                    queue.append(adjNode)
        
        return result


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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends