# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head, cur = list1, list1
        node_a_1, node_b, l2_last = None, None, list2
        for i in range(b + 1):
            if i == a - 1:
                node_a_1 = cur
            if i == b:
                node_b = cur
            cur = cur.next
        while l2_last.next is not None:
            l2_last = l2_last.next

        if a != 0:
            node_a_1.next = list2
        else:
            head = list2
        l2_last.next = node_b.next
        return  head