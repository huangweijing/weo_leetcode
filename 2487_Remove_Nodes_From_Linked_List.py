from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, stk = head, []
        while cur is not None:
            while len(stk) > 0 and stk[-1] < cur.val:
                stk.pop()
            stk.append(cur.val)
            cur = cur.next
        new_head, last_node = None, None
        for val in stk:
            node = ListNode(val)
            if new_head is None:
                new_head = node
            if last_node is not None:
                last_node.next = node
            last_node = node
        return new_head

