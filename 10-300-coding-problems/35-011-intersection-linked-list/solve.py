# Submitted by me as on
# https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1#

'''
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''

#Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1,head2):
    #code here
    curr1,curr2=head1,head2
    while curr1.next and curr2.next:
        curr1=curr1.next
        curr2=curr2.next
    while curr1.next:
        head1=head1.next
        curr1=curr1.next
    while curr2.next:
        head2=head2.next
        curr2=curr2.next    
    while head1 != head2:
        head1=head1.next
        head2=head2.next
    if head1 is None:
        return -1
    else:
        return head1.data
