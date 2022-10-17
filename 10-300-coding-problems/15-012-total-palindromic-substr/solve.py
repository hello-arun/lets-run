# Solutiuon as submitted by me on https://leetcode.com/problems/longest-palindromic-substring/
# The idea is as follows

# We start with a center and check if char at that center could also be the center of a palindrome
# This is create trouble with even length palindrome string 
# To deal with this issue will have two counter in case of odd length palindrom
# the two counters will have same index and in case of even length palindrom two counter will have
# adjacent indices

class Solution:
    def countSubstrings(self, s: str) -> int:
        total = sum(self.counter(s,i,i) + self.counter(s,i,i+1) for i in range(len(s)))
        return total
        
    def counter(self,s,i,j) -> int:
        count=0
        length=len(s)
        while(i>=0 and j<length and s[i]==s[j]):
            count+=1
            i-=1
            j+=1
        return count

