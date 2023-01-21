from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stk_l1, stk_l2 = [], []
        while l1 is not None:
            stk_l1.append(l1)
            l1 = l1.next
        while l2 is not None:
            stk_l2.append(l2)
            l2 = l2.next

        carry, last, head = 0, None, None
        while len(stk_l1) > 0 and len(stk_l2) > 0:
            n1 = stk_l1.pop()
            n2 = stk_l2.pop()
            val = n1.val + n2.val + carry
            carry = val // 10
            head = ListNode(val % 10, last)
            last = head
        while len(stk_l1) > 0:
            n1 = stk_l1.pop()
            val = n1.val + carry
            carry = val // 10
            head = ListNode(val % 10, last)
            last = head
        while len(stk_l2) > 0:
            n2 = stk_l2.pop()
            val = n2.val + carry
            carry = val // 10
            head = ListNode(val % 10, last)
            last = head
        if carry > 0:
            head = ListNode(carry, last)
        return head