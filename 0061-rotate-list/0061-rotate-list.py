# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr = head
        
        while curr:
            n += 1
            curr = curr.next
            
        if n == 0:
            return None
            
        k = k % n
        
        prev1, prev2, prev3, curr1, curr2 = None, None, None, head, head
        
        firstReverse = n - k
                
        while firstReverse != 0:
            nextt = curr1.next
            curr1.next = prev1
            prev1 = curr1
            curr1 = nextt
            
            firstReverse -= 1
            
        while curr1:
            nextt = curr1.next
            curr1.next = prev2
            prev2 = curr1
            curr1 = nextt
            
        curr2.next = prev2
        
        while prev1:
            nextt = prev1.next
            prev1.next = prev3
            prev3 = prev1
            prev1 = nextt
            
        return prev3
