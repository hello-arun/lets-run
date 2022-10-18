#User function Template for python3

class Solution:
    def findPosition(self, N):
        if N==0 or N&(N-1)!=0:
            return -1
        else:
            pos=0
            while N:
                pos+=1
                N>>=1
            return pos
        # code here 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.findPosition(N))
# } Driver Code Ends