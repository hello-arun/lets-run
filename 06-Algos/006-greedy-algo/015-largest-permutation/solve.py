
import enum


def find_largest_perm(A, B):
    """ find the largest permutation
    A: List of integers 1 to N in any order
    B: No of swaps we can make
    """
    i = 0
    _max = len(A)
    d = {x: i for i, x in enumerate(A)}

    while B and i < len(A):
        j = d[_max]
        if i != j:
            B -= 1
            A[i], A[j] = A[j], A[i]
            d[A[i]], d[A[j]] = i, j
        i += 1
        _max -= 1
    return A


if __name__ == "__main__":
    A = [3, 2, 4, 1, 5]
    B = 3
    print(find_largest_perm(A, B))
