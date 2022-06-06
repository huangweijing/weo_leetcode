from typing import List
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def isEnd(self, cur_lists = list[ListNode]):
        for cur_list in cur_lists:
            if cur_list is not None:
                return False
        return True

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_head = None
        last_node = None
        cur_lists = list(lists)
        while not self.isEnd(cur_lists):
            minimum_node = ListNode(val=100000)
            minimum_node_idx = -1
            for i, cur_list in enumerate(cur_lists):
                if cur_list is not None and cur_list.val < minimum_node.val:
                    minimum_node = cur_list
                    minimum_node_idx = i
            cur_node = ListNode()
            cur_node.val = minimum_node.val
            if new_head is None:
                new_head = cur_node
            if last_node is not None:
                last_node.next = cur_node
            last_node = cur_node

            cur_lists[minimum_node_idx] = minimum_node.next

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


l1 = make_link_list([1, 2, 8])
l2 = make_link_list([2, 5, 7])
l3 = make_link_list([4, 9])
sol = Solution()
r = sol.mergeKLists([l1, l2, l3])
print_linked_list(r)
