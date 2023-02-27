#User function Template for python3

class Solution:
    def dfs(self, index, N, adjList, vis):
        vis[index] = 2
        
        for node in adjList[index]:
            if vis[node] == 0:
                if self.dfs(node, N, adjList, vis):
                    return True
            elif vis[node] == 2:
                return True
                
        vis[index] = 1
        return False
    
    def detectCycle(self, N, adjList):
        vis = [0] * N
        
        for i in range(N):
            if vis[i] == 0:
                if self.dfs(i, N, adjList, vis):
                    return True
                    
        return False
    
    def isPossible(self,N,prerequisites):
        #code here
        
        adjList = {}
        
        for i in range(N):
            adjList[i] = []
            
        for task, prereq in prerequisites:
            adjList[prereq].append(task)
            
        return not self.detectCycle(N, adjList)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends