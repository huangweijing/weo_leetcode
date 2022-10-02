from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        cur = head
        node_dict = dict[Node, Node]()
        # rev_node_dict =  dict[Node, Node]()
        while cur is not None:
            new_node = Node(cur.val)
            node_dict[cur] = new_node
            cur = cur.next
        cur = head
        while cur is not None:
            new_node = node_dict[cur]
            new_node.next = node_dict.get(cur.next, None)
            new_node.random = node_dict.get(cur.random, None)
            cur = cur.next

        return node_dict[head]