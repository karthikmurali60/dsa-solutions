# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def countNodes(self, head):
        numNodes = 0
        curr = head
        
        while curr:
            numNodes += 1
            curr = curr.next
        
        return numNodes
        
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None or left == right:
            return head
        
        prev, curr, i = None, head, 1
        numNodes = self.countNodes(head)
        
        while(i != left):
            prev = curr
            curr = curr.next
            i += 1
        
        startNode, endNode = prev, curr
                
        while(i <= right):
            nextt = curr.next
            if i != left:
                curr.next = prev
            prev = curr
            curr = nextt
            i += 1
        
        if left == 1:
            if right == numNodes:
                head.next = None
                return prev
            else:
                head.next = curr
                return prev
        else:
            startNode.next = prev
            endNode.next = curr
        
            return head