# Solution as submitted on https://leetcode.com/problems/valid-parentheses/submissions/
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closing_opening_seq={
            ")":"(",
            "}":"{",
            "]":"["
        }
        for char in s:
            if stack and closing_opening_seq.get(char,None) == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
            
        return len(stack) == 0
