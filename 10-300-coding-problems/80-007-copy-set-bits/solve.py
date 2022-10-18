#User function Template for python3

class Solution:
    def setSetBit(self, x, y, l, r):
        data=0
        for i in range(r-l+1):
            data<<=1
            data|=1
        x|=(y&(data<<(l-1)))
        return x
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        x = int(arr[0])
        y = int(arr[1])
        l = int(arr[2])
        r = int(arr[3])
        
        ob = Solution()
        print(ob.setSetBit(x, y, l, r))
# } Driver Code Ends