# Solution as submitted by me on https://leetcode.com/problems/maximum-product-subarray/
# lets first solve the problem when only positive numbers inclusing zero
# Let's try to use kadane algorithm if possible

# Kadane’s Algorithm
# A very helpful reference to understand the algo is avaialbale at
# https://www.youtube.com/watch?v=YxuK6A3SvTs&t=232s

class Solution:
    def maxProduct(self, arr: List[int]) -> int:
        max_prod_so_far = arr[0]
        max_prod_ending_here = 1 # for positive products
        min_prod_ending_here = 1 # for negative products

        for num in arr:
            max_prod_ending_here,min_prod_ending_here = max(max_prod_ending_here*num, min_prod_ending_here * num),min(min_prod_ending_here * num, max_prod_ending_here*num)
            max_prod_so_far = max(max_prod_so_far,max_prod_ending_here,min_prod_ending_here)
            max_prod_ending_here = max(max_prod_ending_here,1)
            min_prod_ending_here = min(min_prod_ending_here,1)
        return max_prod_so_far
