# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev
        
# Husk neste            nxt = current.next
# Snu pilen             current.next = prez
# Flytt prev fram       prev = current
# Flytt current fram    current = nxt 