# https://www.geeksforgeeks.org/permute-two-arrays-sum-every-pair-greater-equal-k/
# Test if there exist any permutation of two given arrays of equal size such that
# A[i]+B[i] >=k for all i

# Pretty straight forward. just sort one array forward and the other backward and check

# Test 1
a = [2,1,3]
b = [7,8,9]
k = 10

# Test 2
# a = [1, 2, 2, 1]
# b = [3, 3, 3, 4 ]
# k = 5

a.sort(reverse=True)
b.sort()
possible=True
for i in range(len(a)):
    if a[i]+b[i]<k:
        possible=False
        break;
print(possible)