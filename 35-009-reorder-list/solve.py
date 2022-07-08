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
        length=0
        h = head
        while head:
            length+=1
            head=head.next
        head=h
        step=length - length//2
        for i in range(step):
            head = head.next
        head2 = self.rev(head)
        head = h
        for i in range(length//2):
            temp = head.next    # 2
            head.next = head2   # 1>4
            head2 = head2.next  # 3 
            head.next.next=temp # 1>4>2
            head=temp
        head.next=None
        # print(h)
        return h
    
    def rev(self,head):
        prev,curr=None,head
        while curr:
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
        return prev