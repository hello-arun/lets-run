# https://practice.geeksforgeeks.org/problems/product-array-puzzle4525/1#
# See Also 10-012-product-array-itself

class Solution:
    def productExceptSelf(self, nums, n):
        mul=[1]*len(arr)
        l,r = 1,len(arr)-2
        a,b=1,1
        while l<len(arr) and r>-1:
            a*=arr[l-1]
            b*=arr[r+1]
            mul[l] *= a
            mul[r] *= b
            l+=1
            r-=1
        return mul
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends