# Solution as submitted by me on https://leetcode.com/problems/merge-two-sorted-lists/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        if head1 is None and head2 is None:
            return None
        elif head1 is None:
            return head2
        elif head2 is None:
            return head1
        else:
            res = ListNode()
            head = res
            while head1:
                if head2 is None:
                    res.next = head1
                    break
                v1 = head1.val
                v2 = head2.val
                if v1<v2:
                    res.next=head1
                    head1=head1.next
                    res = res.next 
                else:
                    res.next=head2
                    head2=head2.next
                    res=res.next
                if head1 is None:
                    res.next=head2
                    break;
            head = head.next
            return head