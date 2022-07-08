# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode() # Dummy Node
        head = res       # To keep reference of head node 
        while head1 and head2:
            if head1.val < head2.val:
                res.next=head1
                head1=head1.next
            else:
                res.next=head2
                head2=head2.next
            res=res.next
        if head1:
            res.next=head1
        if head2:
            res.next=head2
        return head.next
