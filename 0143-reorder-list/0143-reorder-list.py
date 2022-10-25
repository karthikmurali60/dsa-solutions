# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Reverse 2nd half of Linked List        
        prev, secondHead = None, slow.next
        slow.next = None
        while secondHead:
            nextt = secondHead.next
            secondHead.next = prev
            prev = secondHead
            secondHead = nextt
            
        # Merge first and second halfs
        firstHead, secondHead = head, prev
        while secondHead:
            temp1, temp2 = firstHead.next, secondHead.next
            firstHead.next = secondHead
            secondHead.next = temp1
            firstHead, secondHead = temp1, temp2
            