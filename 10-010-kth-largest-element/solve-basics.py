# Quick-Sort Algorithm
# https://www.geeksforgeeks.org/quick-sort/
# https://en.wikipedia.org/wiki/Quicksort#:~:text=//%20Sorts%20a%20(portion%20of,//%20the%20pivot%20index
# Before solving this problem we need to have a very clear idea # behind the quick-sort approach.
# The most crucial idea behind the quick-sort is that we pick one element
# and our task it put this element at the correct index in the array. if
# this element would be in its correct place then all elemenrs larger than
# this number should be on right side of this and all numbers smaller than
# this number should be on left  side of this. Then we repeat this process
# on the left and right partion and our array is sorted.

def quick_sort(A, lo, hi):
    if lo >= hi or lo < 0:
        return
    # place pivot at right index and place all A[i] <= pivot to left side 
    # and all A[i] > pivot on the right side of pivot
    p = partition(A, lo, hi) 
    quick_sort(A, lo, p-1) # Sort the left  part
    quick_sort(A, p+1, hi) # Sort the right part


def partition(A, lo, hi):
    pivot = A[hi] # We use the right most element as pivot
    # I is used to place pivot at the correct index 
    # why lo-1? think about it (not so hard)
    I = lo-1 
    for j in range(lo, hi+1):
        if A[j] <= pivot:
            I += 1
            A[j], A[I] = A[I], A[j]
    return I

A = [1, 8, 3, 9, 4, 5, 7]
print("Original: ", A)
quick_sort(A, 0, len(A)-1)
print("Sorted:   ", A)
