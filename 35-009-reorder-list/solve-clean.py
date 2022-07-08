# As submitted by me on
# https://leetcode.com/problems/reorder-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        fast = self.rev(slow.next)
        slow = head
        while fast:
            nexts,nextf = slow.next,fast.next
            slow.next = fast
            fast.next = nexts
            fast = nextf
            slow=nexts
        slow.next=None
        return head
    
    def rev(self,head):
        prev,curr=None,head
        while curr:
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
        return prev
