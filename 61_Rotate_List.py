from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        node_cnt = 0
        last_node = None
        while cur is not None:
            node_cnt += 1
            last_node = cur
            cur = cur.next
        if node_cnt == 0:
            return head
        k = node_cnt - k % node_cnt
        last_node.next = head
        idx = 0
        cur = head
        before_head = None
        while idx < k:
            before_head = cur
            cur = cur.next
            idx += 1
        new_head = cur
        before_head.next = None
        return new_head

def print_linked_list(head: ListNode):
    while head is not None:
        print(head.val, end="" if head.next is None else " > ")
        head = head.next
    print()

def make_link_list(data: list[int]) -> ListNode:
    head: ListNode = None
    last_node: ListNode = None
    for e in data:
        node = ListNode(e, None)
        if head is None:
            head = node
        if last_node is not None:
            last_node.next = node
        last_node = node
    return head

data = [1, 2, 3]
ll = make_link_list(data)
print_linked_list(ll)
sol = Solution()
h = sol.rotateRight(ll, 2)
print_linked_list(h)