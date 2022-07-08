# Solution as submitted by me on 
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        dummy=ListNode(0,head)
        length=0
        while head:
            length+=1
            head=head.next
        head = dummy
        length = length-n
        while length>0:
            head = head.next
            length-=1
        print("Node to delete",head.next)
        head.next=head.next.next if head.next else None
        return dummy.next
