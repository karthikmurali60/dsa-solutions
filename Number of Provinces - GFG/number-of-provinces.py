#User function Template for python3

class Solution:
    def dfs(self, node, adjList, vis):
        vis[node] = 1

        for adjNode in adjList[node]:
            if not vis[adjNode]:
                self.dfs(adjNode, adjList, vis)


    def numProvinces(self, adj, V):
        # code here 
        count = 0
        n = len(adj)
        vis = [0] * n

        adjList = {}
        for i in range(n):
            adjList[i] = []

        for i in range(n):
            for j in range(n):
                if i != j and adj[i][j]:
                    adjList[i].append(j)
                    adjList[j].append(i)

        for i in range(n):
            if not vis[i]:
                count += 1
                self.dfs(i, adjList, vis)
        
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends