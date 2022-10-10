# As submitted by me on 
# https://practice.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1

def reverseDLL(head):
    pre,curr=None,head
    while curr:
        nextt=curr.next
        curr.prev = nextt
        curr.next = pre
        pre = curr
        curr = nextt
    return pre
    #return head after reversing
