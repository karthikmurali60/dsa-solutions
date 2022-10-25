# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def countNodes(self, head):
        curr, count = head, 0
        
        while curr:
            count += 1
            curr = curr.next
        
        return count
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        
        numOfNodes = self.countNodes(head)
        i, nodeToRemove = 1, numOfNodes - n + 1
        
        if nodeToRemove == 1:
            head = head.next
            return head
        else:
            prev, curr = None, head
            
            while(i < nodeToRemove):
                prev = curr
                curr = curr.next
                i += 1

            if nodeToRemove == numOfNodes:
                prev.next = None
            else:
                curr.val = curr.next.val
                curr.next = curr.next.next

            return head
        
        
        