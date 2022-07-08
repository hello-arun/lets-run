# Solution as submitted by me on 
# https://practice.geeksforgeeks.org/problems/multiply-two-linked-lists/1/#
MOD = 10**9+7
# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def multiplyTwoList(head1, head2):
    num1,num2=0,0
    while head1:
        num1=num1*10+head1.data
        head1 = head1.next
    while head2:
        num2=num2*10+head2.data
        head2=head2.next
    return (num1*num2)%MOD
    # Code here

