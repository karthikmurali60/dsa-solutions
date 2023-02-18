#User function Template for python3

class Solution:
    def dfs(self, index, adjMatrix, vis):
        if not vis[index]:
            vis[index] = 1
            
            for node in adjMatrix[index]:
                self.dfs(node, adjMatrix, vis)
    
    
    def numProvinces(self, adj, V):
        # code here 
        
        numProvinces = 0
        
        adjMatrix = {}
        
        for i in range(V):
            adjMatrix[i] = []
            
        for u in range(len(adj)):
            for v in range(len(adj[0])):
                if u != v and adj[u][v] == 1:
                    adjMatrix[u].append(v)

        # print(adjMatrix)
        
        vis = [0] * (V + 1)
        
        for i in range(V):
            if not vis[i]:
                numProvinces += 1
                self.dfs(i, adjMatrix, vis)
            
        return numProvinces
        
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