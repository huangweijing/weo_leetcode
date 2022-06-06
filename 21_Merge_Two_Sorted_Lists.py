from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_node1 = list1
        current_node2 = list2
        new_head = None
        current_node_new = ListNode()
        last_node = None
        while current_node1 is not None or current_node2 is not None:
            current_node_new = ListNode()
            if new_head is None:
                new_head = current_node_new

            if current_node2 is None or \
                    (current_node1 is not None and current_node1.val <= current_node2.val):
                current_node_new.val = current_node1.val
                current_node1 = current_node1.next
            elif current_node1 is None or \
                    (current_node2 is not None and current_node2.val <= current_node1.val):
                current_node_new.val = current_node2.val
                current_node2 = current_node2.next
            else:
                continue

            if last_node is not None:
                last_node.next = current_node_new
            last_node = current_node_new

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

list1 = make_link_list([1, 2, 4])
list2 = make_link_list([3, 6, 8])
print_linked_list(list1)
print_linked_list(list2)

sol = Solution()
r = sol.mergeTwoLists(list1, list2)
print_linked_list(r)