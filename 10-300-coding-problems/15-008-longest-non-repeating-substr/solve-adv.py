# Solution as submitted by me on https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Be aware you need to print longest substring and not the sub-sequence

# I think the knuth algorithm might be used here lets try to solve..
class Solution:
    def lengthOfLongestSubstring(self, arr: str) -> int:
        arr_dict = [0] * 128
        start = end = 0
        res = 0
        while end < len(arr):
            r = arr[end]
            arr_dict[ord(r)] += 1

            while arr_dict[ord(r)] > 1:
                l = arr[start]
                arr_dict[ord(l)] -= 1
                start += 1

            res = max(res, end - start + 1)

            end += 1
        return res