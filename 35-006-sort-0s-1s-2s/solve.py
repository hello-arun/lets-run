# Solution as submitted by me on
# https://practice.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1#
# User function Template for python3
'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        if (head == None or head.next == None):
            return head
        h0 = Node(0)
        h1 = Node(0)
        h2 = Node(0)
        h00,h11,h22 = h0,h1,h2

        while head:
            if head.data == 0:
                h0.next = head
                h0 = head
            elif head.data == 1:
                h1.next = head
                h1 = head
            else:
                h2.next = head
                h2 = head
            head = head.next
        if h11.next:
            h0.next=h11.next
        else:
            h0.next=h22.next
        h1.next=h22.next
        h2.next=None
        return h00.next
