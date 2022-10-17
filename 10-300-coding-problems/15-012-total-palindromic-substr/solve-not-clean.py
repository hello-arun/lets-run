# Solutiuon as submitted by me on https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def countSubstrings(self, s: str) -> int:
        numpalin=0
        s1=s.replace("","|")
        center=1
        while center<len(s1)-1:
            rad=0
            while(center-rad-1>=0 and center+rad+1<len(s1) and s1[center-rad-1]==s1[center+rad+1]):
                rad+=1
            if s1[center]=="|":
                numpalin+=(rad//2)
            else:
                numpalin+=ceil(rad/2)
            center+=1
        return (numpalin)
        