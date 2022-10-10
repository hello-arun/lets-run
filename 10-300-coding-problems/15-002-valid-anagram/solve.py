# Solution as submitted on https://leetcode.com/problems/valid-anagram/

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word
# or phrase, typically using all the original letters exactly once.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict={} # Array can also be used but simplicity is more important
        for char in s:
            if char in dict:
                dict[char]+=1
            else:
                dict[char]=1
        for char in t:
            if char in dict and dict[char]>0:
                dict[char] -= 1
            else:
                return False
        return True
        