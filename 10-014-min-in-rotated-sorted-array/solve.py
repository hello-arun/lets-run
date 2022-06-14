# Solution as submitted by me on https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.find_pivot(nums)
            
        
    def find_pivot(self,arr):
        l,r=0,len(arr)-1
        if arr[l]<=arr[r]:
            return arr[l]
        while(l<r):
            mid=(r+l)//2
            if r==l+1:
                return arr[r]
            if arr[mid]>arr[r]:
                l=mid
            else:
                r=mid
            