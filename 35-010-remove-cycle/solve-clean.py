# As submitted by me on 
# https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1/#

'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''
class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        fast,slow=head.next.next,head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return 
            fast=fast.next.next
            slow=slow.next
        K = self.countLoopNodes(fast)
        fast,slow=head,head
        for _ in range(K):
            fast = fast.next
        while slow != fast:
            slow=slow.next
            fast=fast.next
        while(fast.next != slow):
            fast = fast.next
        fast.next = None

    def countLoopNodes(self,loopNode):
        temp=loopNode
        K=1
        while(temp.next != loopNode):
            K+=1
            temp=temp.next
        return K