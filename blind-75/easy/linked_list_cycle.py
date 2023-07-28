# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # next-next pointer
        tortoise = head
        if head:
            hare = head.next

        while tortoise and hare:
            if tortoise == hare:
                return True

            tortoise = tortoise.next
            hare = hare.next
            if hare:
                hare = hare.next
        return False
