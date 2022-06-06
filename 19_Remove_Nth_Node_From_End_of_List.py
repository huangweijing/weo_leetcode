from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def len_of_linked_list(self, head: ListNode) -> int:
        length = 0
        node = head
        while node is not None:
            node = node.next
            length += 1
        return length


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.len_of_linked_list(head)
        if length == n:
            return head.next
        idx = length - n
        node = head
        for i in range(idx - 1):
            node = node.next
        node.next = node.next.next
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

head_node = make_link_list([1,2,3,4,5])
print_linked_list(head_node)

sol = Solution()
head_node = sol.removeNthFromEnd(head_node, 5)
print_linked_list(head_node)