#User function Template for python3

def largest(arr, n):
    largest = -1e9
    
    for num in arr:
        largest = max(largest, num)
        
    return largest

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(largest(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends