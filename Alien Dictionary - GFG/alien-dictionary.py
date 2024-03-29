#User function Template for python3

class Solution:
    def topoSort(self, N, adj):
        indegree = [0] * N
        queue = []
        topo = []
        
        for i in range(N):
            for node in adj[i]:
                indegree[node] += 1
                
        for i in range(N):
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
    
    def find(self, word1, word2):
        m, n = len(word1), len(word2)
        
        left = 0
        
        while left < min(m, n):
            if word1[left] != word2[left]:
                return ord(word1[left]) - ord('a'), ord(word2[left]) - ord('a')
            else:
                left += 1
    
        return None, None
        
    def findOrder(self,dict, N, K):
    # code here
        
        adj = {}
        
        for i in range(K):
            adj[i] = []
            
        for i in range(len(dict) - 1):
            first, second = self.find(dict[i], dict[i + 1])
            
            if first != None and second != None:
                adj[first].append(second)

        topo = self.topoSort(K, adj)
        
        ans = []
        
        for i in range(len(topo)):
            ans.append(chr(topo[i] + ord('a')))
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends