# Solution as submitted on 
# https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1
# If we are allowed to use additional space then the problem is very simple
# but what if we are not? along with a nice constraint

# 0 <= A[i] <= n-1 for all i
# We can use the original array as hash map but we can not directly modify 
# the given array as we could not get original array back?
# Any how we need to find a way to get the original array back!
# Since the values in the array are 0 to n-1 we can use % operator
# See below to understand the great trick

class Solution:
    def duplicates(self, arr, N):
        for ar in arr:
            index = ar%N
            arr[index] += N 
        res=[]
        for i,ar in enumerate(arr):
            if ar/N >= 2:
                res.append(i)
        if len(res)==0:
            return [-1]
        return res

arr = [0,3,3,2]
N=len(arr)
print(Solution().duplicates(arr,N))