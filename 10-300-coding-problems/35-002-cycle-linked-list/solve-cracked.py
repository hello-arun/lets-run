# Solution as submitted on https://leetcode.com/problems/linked-list-cycle/
# Another implementation can be found on the 
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        val_ = -2652682265
        while head is not None:
            if head.val == val_:
                return True
            head.val = val_
            head = head.next
        return False
        