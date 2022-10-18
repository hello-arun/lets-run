# Submitted by me on https://practice.geeksforgeeks.org/problems/count-total-set-bits-1587115620/1
class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        if n==0:
            return 0
        else:
            Num=n&1
            ones=Num
            idx=1
            n>>=1
            N2=1
            while n:
                Num|=(n&1)<<idx
                if n&1:
                    ones+=(N2<<(idx-1))*idx+Num-(N2<<idx)+1
                n>>=1
                idx+=1
            return ones
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends