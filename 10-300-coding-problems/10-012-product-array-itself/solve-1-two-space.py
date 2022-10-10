# https://leetcode.com/problems/product-of-array-except-self/
# Given an integer array nums, return an array answer such that 
# answer[i] is equal to the product of all the elements of nums except nums[i].
# 
# You must write an algorithm that runs in O(n) time and without using the division operation.

# product of all the elements of nums except nums[i] is equal to multiplication of all nums
# to the left of i and multiplication of all nums to right of i
# we will store left and right product in two separate array.

arr=[3,2,4,9]
print(arr)
mul_l=[1]*len(arr)
mul_r=[1]*len(arr)
for i in range(1,len(arr)):
    mul_l[i]=mul_l[i-1]*arr[i-1]
print(" Left mul:",mul_l)

for j in range(len(arr)-2,-1,-1):
    mul_r[j]=mul_r[j+1]*arr[j+1]
print("Right mul:",mul_r)

for j in range(len(arr)):
    mul_l[j]*=mul_r[j]
print("Final mul:",mul_l)
