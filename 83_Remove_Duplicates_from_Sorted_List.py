from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_node: ListNode = head
        last_node = None
        while cur_node != None:
            if last_node is not None and last_node.val == cur_node.val:
                last_node.next = cur_node.next
            else:
                last_node = cur_node
            cur_node = cur_node.next
        return head


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

data = [1, 1, 1, 1]
h = make_link_list(data)
sol = Solution()
sol.deleteDuplicates(h)
print_linked_list(h)