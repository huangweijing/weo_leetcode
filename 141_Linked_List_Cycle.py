# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur1 = head
        cur2 = head
        while cur1 is not None and cur2 is not None and cur2.next is not None:
            cur1 = cur1.next
            cur2 = cur2.next.next
            if cur1 == cur2:
                return True
        return False