# Solutiuon as submitted by me on https://leetcode.com/problems/longest-palindromic-substring/

# The idea is as follows
# All substrs of length 1 are palindrome
# Substrings of lenght 2 are palindrom iff adjacent chars are same.
# Any substring(i,j) of length>2 is palinfrom iff s[i]==s[j] and substr(i+1,j-1) is also palindrom.

# So wee need to make