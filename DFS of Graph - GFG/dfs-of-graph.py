#User function Template for python3

class Solution:
    def dfs(self, index, V, adj, ans, vis):
        if not vis[index]:
            vis[index] = 1
            
            ans.append(index)
            
            for node in adj[index]:
                self.dfs(node, V, adj, ans, vis)
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        
        ans = []
        
        vis = [0] * V

        self.dfs(0, V, adj, ans, vis)
        
        return ans


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