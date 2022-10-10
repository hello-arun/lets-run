# Solution as submitted on https://practice.geeksforgeeks.org/problems/consecutive-elements2306/1#
# Given a string S. For each index i(1<=i<=N-1), erase it if s[i] is equal to s[i-1] in the string.

class Solution:
    def removeConsecutiveCharacter(self, S):
        newS=[S[0]]
        for i in range(1,len(S)):
            if S[i]!=newS[-1]:
                newS.append(S[i])
        return "".join(newS)
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends