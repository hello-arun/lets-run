# Solution as submitted on https://practice.geeksforgeeks.org/problems/count-palindromic-subsequences/1
# Logic is as follows 
# We aim to solve it via recursion, dynamic programming
# Understanding Recursive algorithm is the best part here
# count[i,j] = #palindromic substring from index i to jth both included
# if i==j; count = 1 , otherwise
# We can think that
#       count[i,j] = count[i+1,j] + count[i,j-1] + some correction term
# We need to know this correction term
# if s[i]!=s[j]
#       In this case we know for sure we are couting [i+1,j-1] two times so we just remove that
#       So expression become 
#           count[i,j]=count[i+1,j] + count[i,j-1] -count[i+1,j-1]
# When s[i]==s[j]=x:some char
#       In this Let P is a palim that strictly belongs to [i+1,j-1]. Then xPx will also be a valid palindrom
#       So this time doubl counting is necessary here becuase P and xPx are two different sets of palindroms.
#       In addition, an extra palim 'xx' should be added to the list 
#       So expression become 
#           count[i,j]=count[i+1,j] + count[i,j-1] + 1

class Solution:
    def __init__(self):
        self.memo=""
    
    def count(self,s,i,j):
        if i>j:
            return 0
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        if i==j:
            self.memo[i][j]=1
            return 1
        elif s[i]==s[j]:
            count=self.count(s,i+1,j)+self.count(s,i,j-1)+1
            self.memo[i][j]=count
            return count
        else:
            count= self.count(s,i+1,j)+self.count(s,i,j-1)-self.count(s,i+1,j-1)
            self.memo[i][j]=count
            return count
    
    def countPS(self,string):
        self.memo=[[-1 for i in string] for j in string]
        num=1000000007
        return self.count(string,0,len(string)-1)%num

#{ 
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        ob=Solution()
        print(ob.countPS(input().strip()))

# } Driver Code Ends