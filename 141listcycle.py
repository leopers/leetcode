# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
            
        i1 = head
        i2 = head.next

        while i1 != i2:
            if not i2 or not i2.next:
                return False
            i1 = i1.next
            i2 = i2.next.next

        return True