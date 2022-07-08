# This is very clever
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/1401309/Single-pass-python-solution-or-O(N)-or-Easy-or-SR
# Basic idea behind this implementation is that
# We forward one pointer by n position and then move forward and then start moving both pointers
# When the first pointer reach the end we are at the correct position to determine which node to remove
# Try to understand it, very easy(may be not)

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    i,j=head, head
    for k in range(n):
        j = j.next
    #now i and j will be at difference n
    if j == None: #Only happens when we are supposed to remove the first element
        return head.next
    while j.next != None:
        i = i.next
        j = j.next
    i.next = i.next.next
    return head