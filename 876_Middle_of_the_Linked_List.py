from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = head, head
        while node2 is not None:
            if node2.next is not None:
                node2 = node2.next
            else:
                break
            if node2.next is not None:
                node2 = node2.next
            node1 = node1.next

        return node1