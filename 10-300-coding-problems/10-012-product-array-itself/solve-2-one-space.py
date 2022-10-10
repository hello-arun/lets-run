# https://leetcode.com/problems/product-of-array-except-self/
# Given an integer array nums, return an array answer such that 
# answer[i] is equal to the product of all the elements of nums except nums[i].
# 
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Instead of using two arrays as we used in case solve-1.py we only use a temp variable
# here to solve the problem.

arr=[3,2,4,9]
print(arr)
mul=[1]*len(arr)
for i in range(1,len(arr)):
    mul[i]=mul[i-1]*arr[i-1]
print(" Left mul:",mul)
temp=1
for j in range(len(arr)-1,-1,-1):
    mul[j]*=temp
    temp*=arr[j]
print("Final mul:",mul)

# for j in range(len(arr)):
#     mul[j]*=mul[j]
# print("Final mul:",mul)
