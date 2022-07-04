from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = nextclass Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is None:
        #     return head

        last_tail = None
        new_head = None
        cur = head
        while cur is not None:
            cur_val = cur.val
            first_node = cur
            cur_val_cnt = 0
            while cur is not None and cur_val == cur.val:
                cur = cur.next
                cur_val_cnt += 1
                continue
            # print(cur_val, cur_val_cnt)
            if cur_val_cnt == 1:
                if last_tail is not None:
                    last_tail.next = first_node
                if new_head is None:
                    new_head = first_node
                last_tail = first_node

        if last_tail is not None:
            last_tail.next = None
        return new_head



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

ll = make_link_list([])
print_linked_list(ll)
sol = Solution()
ll = sol.deleteDuplicates(ll)
print_linked_list(ll)