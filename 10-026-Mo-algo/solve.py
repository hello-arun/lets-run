# https://www.geeksforgeeks.org/mos-algorithm-query-square-root-decomposition-set-1-introduction/
# Let us consider the following problem to understand MO’s Algorithm.
# We are given an array and a set of query ranges, we are required to find the sum of every query range.

# Example: 

# Input:  arr[]   = {1, 1, 2, 1, 3, 4, 5, 2, 8};
#         query[] = [0, 4], [1, 3] [2, 4]
# Output: Sum of arr[] elements in range [0, 4] is 8
#         Sum of arr[] elements in range [1, 3] is 4  
#         Sum of arr[] elements in range [2, 4] is 6

arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
sums= [0]*(len(arr)+1)
queries = [[0,4],[1,3],[2, 4]]
for i in range(1,len(arr)):
    sums[i]=sums[i-1]+arr[i-1]

for query in queries:
    print(f"Query: {query}, Sum: {sums[query[1]+1]-sums[query[0]]}") 
