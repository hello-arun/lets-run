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
        arr_dict={}
        max_len_so_far = 0
        max_len_ending_here = 0
        start=-1

        for i,num in enumerate(arr):
            if not num in arr_dict:
                arr_dict[num] = i
            else:
                if arr_dict[num]>start:
                    start=arr_dict[num]
                arr_dict[num] = i
            max_len_ending_here = i-start

            if max_len_so_far < max_len_ending_here:
                max_len_so_far = max_len_ending_here
        return max_len_so_far
