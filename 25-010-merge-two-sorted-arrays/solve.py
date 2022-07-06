# Solution as submitted by me on 
# https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1#
# A very helpful video link to understand the solution 
# https://www.youtube.com/watch?v=hVl2b3bLzBw

# Connection with it's soul is still pending

class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,m, n):
        gap=self.nextGap(m+n)
        while(gap>0):
            i=0
            j=i+gap
            while(j<m+n and i < m+n):
                if i>=m:
                    ii=i-m
                    jj=j-m
                    if arr2[ii] > arr2[jj]:
                        arr2[ii],arr2[jj]=arr2[jj],arr2[ii]
                elif j>=m:
                    ii=i
                    jj=j-m
                    if arr1[ii] > arr2[jj]:
                        arr1[ii],arr2[jj]=arr2[jj],arr1[ii]
                else:
                    ii=i
                    jj=j
                    if arr1[ii] > arr1[jj]:
                        arr1[ii],arr1[jj]=arr1[jj],arr1[ii]
                i+=1
                j+=1
            gap = self.nextGap(gap)
    
    def nextGap(self,gap):
        if gap<=1:
            return 0
        return (gap // 2) + (gap % 2)
            # print(arr1,i,arr2)
        #code here
    
#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code Ends