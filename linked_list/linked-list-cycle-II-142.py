# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# This problem can be solved by using 2 approaches:
# 1. Using Set (TC: O(n) and SC: O(n))
# 2. Floyd's Tortoise and Hare (TC: O(n) and SC: O(1)) [Better Approach]
# Below is solution for approach 2.

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None or head.next is None):
            return

        slow, fast = head, head

        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next

            if(slow == fast):
                break

        # If there is no loop, then return
        if(fast is None or fast.next is None):
            return

        slow = head
        while(slow != fast):
            slow = slow.next
            fast = fast.next

        return fast
