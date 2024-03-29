# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2Lists(self, list1, list2):
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        
        temp = ListNode()
        head = temp
        
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
                
            temp = temp.next
            
        if list1:
            temp.next = list1
        
        if list2:
            temp.next = list2
            
        return head.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                
                mergedLists.append(self.merge2Lists(list1, list2))
                
            lists = mergedLists
            
        return lists[0]
        
        