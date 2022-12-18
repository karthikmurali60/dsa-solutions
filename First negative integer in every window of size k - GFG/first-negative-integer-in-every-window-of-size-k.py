#User function Template for python3

def printFirstNegativeInteger( A, N, K):
    # code here
    i, j = 0, 0
    result = []
    tempList = []
    
    while j < N:
        if A[j] < 0:
            tempList.append(A[j])
            
        if j - i + 1 < K:
            j += 1
        else:
            if len(tempList) == 0:
                result.append(0)
            else:
                result.append(tempList[0])
                
                if tempList[0] == A[i]:
                    tempList.pop(0)
                
            i += 1
            j += 1
        
    return result
            
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends