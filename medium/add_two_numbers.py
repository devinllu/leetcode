# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = False
        init = False
        
        head = ListNode(0, None)
        
        current = head
        
        while l1 or l2:
            
            total = 0
            
            if l1:
                total += l1.val
                l1 = l1.next
            
            if l2:
                total += l2.val
                l2 = l2.next
                
            if carry:
                carry = False
                total += 1
            node_val = total
            
            if total >= 10:
                carry = True
                node_val = total % 10
                
            if not init:
                init = True
                current.val = node_val
            else:
                new_node = ListNode(node_val, None)
                current.next = new_node
                current = current.next
        if carry:
            new_node = ListNode(1, None)
            current.next = new_node
        
        return head
                

            