# Soluiton as submitted by me on
# https://practice.geeksforgeeks.org/problems/linked-list-in-zig-zag-fashion/1#
# https://www.geeksforgeeks.org/linked-list-in-zig-zag-fashion/

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    def zigzag(self, head):
        z=True
        curr=head
        while curr.next:
            if z:
                if curr.next.data<curr.data:
                    curr.data,curr.next.data = curr.next.data,curr.data
            else:
                if curr.next.data>curr.data:
                    curr.data,curr.next.data = curr.next.data,curr.data
            curr=curr.next
            z = not z
        return head
 