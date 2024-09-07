#Definition for singly-linked list.

import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 1

        Head = ListNode(0, head)

        while head.next != None: 
            head = head.next 
            n+=1

        head.next = Head.next

        k = k%n

        node1 = Head.next
        node2 = Head.next.next
        for i in range(n-k-1):
            node1 = node1.next
            node2 = node2.next

        node1.next = None
        return node2