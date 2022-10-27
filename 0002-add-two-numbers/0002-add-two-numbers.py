# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        resultHead = ListNode()
        curr = resultHead
        
        while l1 and l2:
            currSum = l1.val + l2.val + carry
            val = currSum % 10
            carry = currSum // 10
            
            tempNode = ListNode(val)
            curr.next = tempNode
            curr = tempNode
            
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            currSum = l1.val + carry
            val = currSum % 10
            carry = currSum // 10
            
            tempNode = ListNode(val)
            curr.next = tempNode
            curr = tempNode
            
            l1 = l1.next
        
        while l2:
            currSum = l2.val + carry
            val = currSum % 10
            carry = currSum // 10
            
            tempNode = ListNode(val)
            curr.next = tempNode
            curr = tempNode
            
            l2 = l2.next
            
        if carry:
            tempNode = ListNode(carry)
            curr.next = tempNode
            curr = tempNode
            
        return resultHead.next