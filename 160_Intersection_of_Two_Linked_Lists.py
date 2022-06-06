from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur = headA
        node_map = dict[int, ListNode]()
        while cur is not None:
            node_map[id(cur)] = cur
            cur = cur.next

        cur = headB
        while cur is not None:
            if id(cur) in node_map:
                return cur
            cur = cur.next
        return None

# Sample Solution
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         one = headA
#         two = headB
#
#         while one != two:
#             one = headB if one is None else one.next
#             two = headA if two is None else two.next
#         return one


