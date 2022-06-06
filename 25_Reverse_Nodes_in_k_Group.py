from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        node_list = list[ListNode]()
        cur_node = head
        while cur_node is not None:
            node_list.append(cur_node)
            cur_node = cur_node.next

        for i, node in enumerate(node_list):
            if i % k == 0:
                if i + k <= len(node_list):
                    tmp_stack = list()
                    for j in range(k):
                        tmp_stack.append(node_list[i + j])
                    # print(tmp_stack)
                    for j in range(k):
                        node_list[i + j] = tmp_stack.pop()

        for i, node in enumerate(node_list):
            if i + 1 < len(node_list):
                node.next = node_list[i + 1]
        if len(node_list) > 0:
            node_list[len(node_list) - 1].next = None

        return None if len(node_list) == 0 else node_list[0]


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


list1 = make_link_list([2, 1])
sol = Solution()
r = sol.reverseKGroup(list1, 2)
print_linked_list(r)