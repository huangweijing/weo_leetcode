from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_hash = dict[ListNode, int]()
        cur = head
        # pos = 0
        while cur is not None:
            if cur in node_hash.keys():
                return cur
            else:
                node_hash[cur] = pos
            cur = cur.next
            # pos += 1
        return None