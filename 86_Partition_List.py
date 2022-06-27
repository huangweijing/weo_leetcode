from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self):
        self.pre_node = dict[ListNode, ListNode]()
        self.tail: ListNode = None
        self.pivot: ListNode = None

    # insert node after node2
    def move_after(self, node: ListNode, node2: ListNode, head: ListNode) -> ListNode:
        if node == node2 or (node2 is not None and node2.next == node):
            return head

        node_pre = self.pre_node[node]
        node_next = node.next
        node2_next = node2.next
        # print(f"node_pre={node_pre}, node_next={node_next}, node2_next={node2_next}")
        if node_pre is not None:
            # print(f"no need new head: {node_pre.val}")
            node_pre.next = node_next
        else:
            head = node_next
            # print(f"new head: {head.val}")
        self.pre_node[node_next] = node_pre
        # print(head.val)

        node2.next = node
        if node2_next is not None:
            self.pre_node[node2_next] = node
        node.next = node2_next
        self.pre_node[node] = node2

        return head

    def swap_node(self, node1: ListNode, node2: ListNode):
        swap = node1.val
        node1.val = node2.val
        node2.val = swap

    def scan_list(self, head: Optional[ListNode], x: int):
        cur = head
        self.pre_node[head] = None
        while cur is not None:
            if x == cur.val:
                self.pivot = cur
            if cur.next is not None:
                self.pre_node[cur.next] = cur
            else:
                self.tail = cur
            cur = cur.next
            x -= 1

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        self.scan_list(head, x)
        cur = head
        first_moved = None
        while cur is not None and cur != first_moved:
            cur_next = cur.next
            if cur.val >= x:
                head = self.move_after(cur, self.tail, head)
                self.tail = cur
                if first_moved is None:
                    first_moved = cur

            cur = cur_next

        return head



def print_linked_list(head: ListNode, txt=""):
    print(f"{txt} ", end="")
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

# data = ([1,4,3,2,5,2], 3)
data = ([2, 1], 2)
ll = make_link_list(data[0])
print_linked_list(ll, "start:")
sol = Solution()
r = sol.partition(ll, data[1])
# sol.scan_list(ll, 2)
# ll = sol.move_after(ll, ll.next, ll)
print_linked_list(r, "end:  ")