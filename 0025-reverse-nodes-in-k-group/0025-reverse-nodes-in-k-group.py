# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode
        dummy.next = head
        
        curr = head
        nodeCount = 0
        while curr:
            nodeCount += 1
            curr = curr.next
            
        prev = curr = nxt = dummy
        
        while nodeCount >= k:
            curr = prev.next
            nxt = curr.next
            
            for i in range(1, k):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next
                
            prev = curr
            nodeCount -= k
            
        return dummy.next