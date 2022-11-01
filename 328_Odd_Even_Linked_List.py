from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        odd_head, even_head = head, head.next
        odd_cur, even_cur = odd_head, even_head
        cur = head.next.next
        odd_head.next, even_head.next = None, None
        is_odd = True
        while cur is not None:
            if is_odd:
                odd_cur.next = cur
                odd_cur = cur
            else:
                even_cur.next = cur
                even_cur = cur

            is_odd = not is_odd
            old_cur = cur
            cur = cur.next
            old_cur.next = None

        odd_cur.next = even_head
        return odd_head


