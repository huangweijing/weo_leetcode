from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_from_head(head: ListNode):
    cur = head
    while cur is not None:
        print(f"{cur.val} > ", end="")
        cur = cur.next
    print()

def build_from_list(data: list[int]):
    head = None
    last_node = None
    for num in data:
        node = ListNode(num)
        if head is None:
            head = node
        if last_node is not None:
            last_node.next = node
        last_node = node
    return head


class Solution:

    def insert_node(self, head: ListNode, node: ListNode) -> ListNode:
        cur = head
        last_node = None
        while cur is not None:
            if node.val <= cur.val:
                break
            last_node = cur
            cur = cur.next

        if last_node is None:
            node.next = head
            head = node
        else:
            last_node.next = node
            node.next = cur
        return head

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        cur = head
        while cur is not None:
            cur_next = cur.next
            new_head = self.insert_node(new_head, cur)
            cur = cur_next
        return new_head

ll = build_from_list([3, 4, 2, 7, 1])
ll = Solution().insertionSortList(ll)
print_from_head(ll)
