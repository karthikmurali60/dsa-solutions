"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here

        prev, curr, nextt = None, head, head.next

        while(nextt is not None):
            curr.next = prev
            prev = curr
            curr = nextt
            nextt = nextt.next

        curr.next = prev

        return curr
