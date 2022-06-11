# Solution as I submitted on leetCode
# https://leetcode.com/problems/contains-duplicate/submissions/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates={}
        for num in nums:
            if num in duplicates:
                return True
            else :
                duplicates[num]=1
        return False