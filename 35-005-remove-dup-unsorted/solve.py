# As submitted by me on 
# https://practice.geeksforgeeks.org/problems/remove-duplicates-from-an-unsorted-linked-list/

'''
    # Node Class
    class Node:
        def __init__(self, data):   # data -> value stored in node
            self.data = data
            self.next = None
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        dict={}
        res = head
        last = head
        while head:
            if not head.data in dict:
                dict[head.data]=True
                last = head 
            else:
                last.next = head.next
            head = head.next
        return res
        # return head after editing list

