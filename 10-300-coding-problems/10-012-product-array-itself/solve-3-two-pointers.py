# https://leetcode.com/problems/product-of-array-except-self/
# Given an integer array nums, return an array answer such that 
# answer[i] is equal to the product of all the elements of nums except nums[i].
# 
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Solve-2 was better but I can do one better. I use two pointers here runing left and right and try to
# accomplish this task in only single loop

arr=[3,2,4,9]
print(arr)
mul=[1]*len(arr)
l,r = 1,len(arr)-2
a,b=1,1
while l<len(arr) and r>-1:
    a*=arr[l-1]
    b*=arr[r+1]
    mul[l] *= a
    mul[r] *= b
    l+=1
    r-=1

print("Final mul:",mul)
