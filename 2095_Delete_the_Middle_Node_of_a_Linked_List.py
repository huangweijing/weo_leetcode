from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        cur, cur2, prev = head, head.next, None
        while cur2 is not None:
            prev = cur
            cur = cur.next
            cur2 = cur2.next
            if cur2 is None:
                break
            cur2 = cur2.next

        prev.next = prev.next.next
        return head

