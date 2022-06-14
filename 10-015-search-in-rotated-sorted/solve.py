# As submitted by me on https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot=self.find_pivot(nums)
        print("pivot index",pivot)
        index = self.bin_search(nums,target,0,max(pivot-1,0))
        if index is not None:
            return index
        else:
            index = self.bin_search(nums,target,pivot,len(nums)-1)
            if index is not None:
                return index
            else:
                return -1

    def find_pivot(self,arr):
        l,r=0,len(arr)-1
        if arr[l]<=arr[r]:
            return 0
        while(l<r):
            mid=(r+l)//2
            if arr[mid]>arr[r]:
                l=mid
            else:
                r=mid
            if r==l+1:
                return r
            

    def bin_search(self,arr,element,l,r):
        while l <= r:
            mid = (r+l) // 2

            # if element at mid
            if arr[mid] == element:
                return mid 
            # If element is greater, ignore left half
            elif arr[mid] < element:
                l = mid + 1 
            # If x is smaller, ignore right half
            else:
                r = mid - 1
        return None

