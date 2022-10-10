# Solution as submitted on https://leetcode.com/problems/linked-list-cycle/
# Another implementation can be found on the 
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dict={}
        while head is not None:
            if head in dict:
                return True
            else:
                dict[head]=True
            head = head.next
        return False