# https://leetcode.com/problems/next-permutation/
# Three step solution
# 1. Start from the right side and find i and i-1 such that A[i]>A[i-1] 
# 2. Swap A[i-1] with least larger number from A[i:]
# 3. reverse A[i:]

def reverse(arr,l,r):
    # To reverse elements in betweeb left and right index
    while(l<r):
        arr[l],arr[r] = arr[r],arr[l] # Sweet swap code
        l+=1
        r-=1

A=[1,4,3,2]
I=len(A)-1
print("original",A)
# Step 1
while I>0:
    if A[I]>A[I-1]:
        break
    else:
        I-=1

if I==0:
    reverse(A,0,len(A))
    print("Next Permutation not possible",A)
else:
    # Step 2
    J=I # least larger number index
    least_diff=A[I]-A[I-1]
    for i in range(I,len(A)):
        c_diff=A[i]-A[I-1]
        if c_diff>0:
            if c_diff<least_diff:
                least_diff = c_diff
            J=i
        else:
            break
    A[I-1],A[J] = A[J],A[I-1]
    
    # Step 3
    reverse(A,I,len(A)-1)
    print("Next Permutation",A)



