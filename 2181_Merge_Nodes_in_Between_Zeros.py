from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        cur = cur.next
        merged_sum = 0
        new_cur = None
        new_head = None
        while cur is not None:
            if cur.val == 0:
                new_node = ListNode(val=merged_sum)
                if new_head is None:
                    new_head = new_node
                    new_cur = new_node
                else:
                    new_cur.next = new_node
                    new_cur = new_node

                merged_sum = 0
            else:
                merged_sum += cur.val
            cur = cur.next

        return new_head