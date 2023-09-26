from typing import Optional


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def expand(self, cur: Node, cur_next: Node):
        # print(cur.prev, cur.next, cur.val, cur.child)
        child_head = cur.child
        child_last = None
        child_cur = cur.child
        while child_cur is not None:
            child_last = child_cur
            child_cur_next = child_cur.next
            if child_cur.child is not None:
                self.expand(child_cur, child_cur_next)
            child_cur = child_cur.next

        cur.child = None
        cur.next = child_head
        child_head.prev = cur
        child_last.next = cur_next
        if cur_next is not None:
            cur_next.prev = child_last


    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        while cur is not None:
            cur_next = cur.next
            if cur.child is not None:
                self.expand(cur, cur_next)
            cur = cur_next

        return head
