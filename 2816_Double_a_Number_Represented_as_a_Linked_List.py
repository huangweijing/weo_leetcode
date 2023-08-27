from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(0, head)
        stk = [new_head]
        cur: ListNode = head
        while cur is not None:
            stk.append(cur)
            cur = cur.next
        carry = 0
        while len(stk) > 0:
            node = stk.pop()
            double_val = node.val * 2 + carry
            if double_val >= 10:
                carry = 1
                node.val = double_val - 10
            else:
                carry = 0
                node.val = double_val
        if new_head.val > 0:
            return new_head
        else:
            return new_head.next