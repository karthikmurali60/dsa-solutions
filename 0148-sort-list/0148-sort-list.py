# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        arr = []
        
        curr = head
        
        while curr:
            arr.append(curr.val)
            curr = curr.next
            
        arr.sort()
        
        head = ListNode(arr[0])
        
        curr = head
        
        for i in range(1, len(arr)):
            node = ListNode(arr[i])
            
            curr.next = node
            
            curr = node
            
        return head