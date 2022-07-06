# Solution as submitted by me on 
# https://practice.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1/#
# Given an array Arr of size N containing positive integers. Find the maximum sum
# of a subsequence such that no two numbers in the sequence should be adjacent in the array.

def findMaxSum(arr):
    # At every index we want to keep track of the max sum
    # possible including that number and excluding that num
    
    max_sum_incl=0 # max sum including 
    max_sum_excl=0 # max sum excluding
    
    max_sum = 0
    i=0
    for num in arr:
        max_sum_incl_ = max_sum_excl+num
        max_sum_excl  = max(max_sum_incl,max_sum_excl)
        max_sum_incl  = max_sum_incl_
        max_sum = max(max_sum_incl,max_sum_excl)
        print(i,max_sum_incl,max_sum_excl)
        i+=1
    return max_sum

arr = [3, 2, 7, 10]
print(findMaxSum(arr))