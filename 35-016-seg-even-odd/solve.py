# https://practice.geeksforgeeks.org/problems/segregate-even-and-odd-nodes-in-a-linked-list5035/1#

# Following is the structure of node 
# class Node:
#     def __init__(self):  
#         self.data = None
#         self.next = None

class Solution:
    def divide(self, N, head):
        if not head.next:
            return head
        curr,prev=head,node()
        prev.next=head
        even,res=prev,prev
        while curr:
            nextt=curr.next
            if curr.data%2==0:
                if even.next != curr:
                    odd = even.next
                    even.next = curr
                    curr.next = odd
                    even = curr
                    curr = nextt
                    prev.next = curr
                else:
                    prev=curr
                    curr=nextt
                    even=even.next
            else:
                prev = curr
                curr = nextt
        return res.next
        