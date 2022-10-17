# Solutiuon as submitted by me on https://leetcode.com/problems/longest-palindromic-substring/
# The idea is as follows

# We start with a center and check if char at that center could also be the center of a palindrome
# This is create trouble with even length palindrome string 
# To deal with this issue we insert `|` in between all chars and also at start and the end.
# This way all even length palindrom are converted to odd length e.g. ABBA > |A|B|B|A|

# We just keep track of larget palindrome and and update if bigger palindrome is obtained
class Solution:
    def longestPalindrome(self, s: str) -> str:
        palin=""
        s1=s.replace("","|")
        center=1
        while center<len(s1)-1:
            rad=0
            while(center-rad-1>=0 and center+rad+1<len(s1) and s1[center-rad-1]==s1[center+rad+1]):
                rad+=1
            if 2*rad+1>len(palin):
                palin=s1[center-rad:center+rad+1]
            center+=1
        out=palin.replace("|","")
        return out
        
    
