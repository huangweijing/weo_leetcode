import math
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next is not None:

            new_node = ListNode(val=math.gcd(cur.val, cur.next.val)
                                , next=cur.next)
            next_node = cur.next
            cur.next = new_node
            cur = next_node
        return head