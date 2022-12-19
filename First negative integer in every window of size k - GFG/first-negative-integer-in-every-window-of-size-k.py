#User function Template for python3

def printFirstNegativeInteger( A, N, K):
    # code here
    calculationsList = []
    ansList = []
    
    i, j = 0, 0
    
    while j < N:
        # Do the calculations
        if A[j] < 0:
            calculationsList.append(A[j])
            
        if j - i + 1 < K:
            j += 1
        else:
            # Pick answer from the calculations
            if len(calculationsList) == 0:
                ansList.append(0)
            else:
                ansList.append(calculationsList[0])
                
                # Slide the window
                if A[i] == calculationsList[0]:
                    calculationsList.pop(0)
            
            i += 1
            j += 1
    
    return ansList


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