# We extend the finding of Quick-Sort algorithm in this Part
# We want to find the Kth Smallest number. It means in a 
# sorted array A we want to get the number at index = K-1
# i.e 
# 1st Smallest = 0th index element in array
# 2nd Smallest = 1st index element 

# Algo : We chose a pivot point and partition the array
# if pivot-index == K-1 we return the number
# if pivot-index is < K-1 we partition the right part
# if pivot index is > K-1 we partition the left half


def quick_sort(A,K, lo, hi):
    if lo >= hi or lo < 0:
        return
    # place pivot at right index and place all A[i] <= pivot to left side 
    # and all A[i] > pivot on the right side of pivot
    p = partition(A, lo, hi) 
    if p == K-1:
        return
        # print(A[p])
        # return A[p]
    elif p < K-1:
        quick_sort(A,K,p+1,hi) # Sort the right part
    else:
        quick_sort(A,K,lo,p-1) # Sort the left  part


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

A = [1, 8, 4, 9, 5, 3, 7]
K = 7
print("        Original:", A)
quick_sort(A,K, 0, len(A)-1)
print("Partially Sorted:", A)
print(f"{K}th Smallest:", A[K-1])