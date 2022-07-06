# https://www.geeksforgeeks.org/find-a-pair-with-the-given-difference/
# Given an unsorted array and a number n, find if there exists a pair 
# of elements in the array whose difference is n. 

def find_pair(arr,n):
    small, big = 0, 1
    while big > small:
        diff = arr[big]-arr[small]
        if (diff == n):
            return arr[small],arr[big]
        elif (diff<n):
            big+=1
        elif (diff>n):
            small+=1


# Test 1
arr = [2, 3, 5, 20, 50, 80]  # We assume array is already sorted
n = 77

# Test 2
# arr = [1, 8, 30, 40, 100] # We assume array is already sorted
# n = 32

print(find_pair(arr,n))