
# Solution as submitted by me on https://www.interviewbit.com/problems/repeat-and-missing-number-array/
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        count=[0]*len(A)
        for num in A:
            count[num-1]+=1
        for i,num in enumerate(count):
            if num==0:
                B=i+1
            if num==2:
                A=i+1
        return A,B
