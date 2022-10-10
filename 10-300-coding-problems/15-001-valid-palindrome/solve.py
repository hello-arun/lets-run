# Solution as submitted on https://leetcode.com/problems/valid-palindrome/

# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads
# the same forward and backward. Alphanumeric characters include letters 
# and numbers.Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        i,j=0,len(s)-1 # Two Pointers
        while(j>i):
            if not self.isValidAlphaNumeric(s[i]):
                i+=1
            elif not self.isValidAlphaNumeric(s[j]):
                j-=1
            else:
                if s[i] == s[j]:
                    i+=1
                    j-=1
                else:
                    return False
        return True
        
    
    def isValidAlphaNumeric(self,char) -> bool:
        return (char>='a' and char<='z') or (char>='0' and char<='9')
        
        