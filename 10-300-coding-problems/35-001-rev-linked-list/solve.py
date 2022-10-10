# Solution as submitted https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        tail = head.next
        head.next = None
        while tail != None:
            temp = tail.next
            tail.next = head
            head = tail
            tail = temp
        return head
