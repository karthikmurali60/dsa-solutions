#User function Template for python3

class Solution:
    def dfs(self, node, adj, result, vis):
        if vis[node]:
            return
        
        vis[node] = 1
        
        result.append(node)
        
        for adjNode in adj[node]:
            self.dfs(adjNode, adj, result, vis)
        
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        result = []
        vis = [0] * len(adj)
        
        self.dfs(0, adj, result, vis)
        
        return result


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends