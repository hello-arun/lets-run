# Solution as submitted by me on leet-code
class Solution:
    def quick_sort(self,A,K, lo, hi):
        if lo >= hi or lo < 0:
            return
        # place pivot at right index and place all A[i] <= pivot to left side 
        # and all A[i] > pivot on the right side of pivot
        p = self.partition(A, lo, hi) 
        if (p==len(A)-K):
            return
            # print(A[p])
            # return A[p]
        elif p<len(A)-K:
            self.quick_sort(A,K, p+1, hi) # Sort the right part
        else:
            self.quick_sort(A,K,lo, p-1) # Sort the left  part

    def partition(self,A, lo, hi):
        pivot = A[hi] # We use the right most element as pivot
        # I is used to place pivot at the correct index 
        # why lo-1? think about it (not so hard)
        I = lo-1 
        for j in range(lo, hi+1):
            if A[j] <= pivot:
                I += 1
                A[j], A[I] = A[I], A[j]
        return I
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quick_sort(nums,k,0,len(nums)-1)
        return nums[len(nums)-k]

