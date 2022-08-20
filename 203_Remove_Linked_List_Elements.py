from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        new_head = head
        prev = None
        while cur is not None:
            cur_next = cur.next
            if cur.val == val:
                if prev is None:
                    new_head = cur_next
                else:
                    prev.next = cur_next
            else:
                prev = cur
            cur = cur_next

        return new_head