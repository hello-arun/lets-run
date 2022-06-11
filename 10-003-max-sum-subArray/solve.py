# Kadane’s Algorithm
# A very helpful reference to understand the solution is avaialbale at
# https://www.youtube.com/watch?v=YxuK6A3SvTs&t=232s
arr=[-2, -3, 4, -1, -2, 1, 5, -3]
max_sum_so_far = arr[0]
max_sum_ending_here=0
for num in arr:
    max_sum_ending_here = max_sum_ending_here + num
    if (max_sum_so_far < max_sum_ending_here):
        max_sum_so_far = max_sum_ending_here

    if max_sum_ending_here < 0:
        max_sum_ending_here = 0  
print(max_sum_so_far)