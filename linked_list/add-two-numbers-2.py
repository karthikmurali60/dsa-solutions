# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sums = 0
        carry = 0
        c1 = l1
        c2 = l2

        if(c1.val + c2.val > 9):
            sums = int((c1.val + c2.val)%10)
            carry = 1
        else:
            sums = c1.val + c2.val

        newHead = ListNode(sums, None)

        c1 = l1.next
        c2 = l2.next
        c3 = newHead

        while(c1 is not None and c2 is not None):
            if(c1.val + c2.val + carry > 9):
                sums = int((c1.val + c2.val + carry)%10)
                carry = 1
            else:
                sums = c1.val + c2.val + carry
                carry = 0

            tempNode = ListNode(sums, None)
            c3.next = tempNode

            c1 = c1.next
            c2 = c2.next
            c3 = c3.next

        while(c1 is not None):
            if(c1.val + carry > 9):
                sums = int((c1.val + carry)%10)
                carry = 1
            else:
                sums = c1.val + carry
                carry = 0

            tempNode = ListNode(sums, None)
            c3.next = tempNode

            c1 = c1.next
            c3 = c3.next

        while(c2 is not None):
            if(c2.val + carry > 9):
                sums = int((c2.val + carry)%10)
                carry = 1
            else:
                sums = c2.val + carry
                carry = 0

            tempNode = ListNode(sums, None)
            c3.next = tempNode

            c2 = c2.next
            c3 = c3.next

        if(carry == 1):
            tempNode = ListNode(1, None)
            c3.next = tempNode

        return newHead
