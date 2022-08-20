class LinkedNode:
    def __init__(self):
        self.prev: LinkedNode = None
        self.next: LinkedNode = None
        self.val: int = 0
        self.key: int = 0

class DoubleLinkedList:
    def __init__(self):
        self.head: LinkedNode = None
        self.tail: LinkedNode = None
        self.length = 0

    # node should be in the list
    def remove(self, node: LinkedNode) -> LinkedNode:
        self.length -= 1
        if node.prev is None: # head
            if node.next is None:
                self.head = None
                self.tail = None
            else:
                node.next.prev = None
                self.head = node.next
            node.next = None
            node.prev = None
            return node
        if node.next is None: # tail
            if node.prev is None:
                self.head = None
                self.tail = None
            else:
                node.prev.next = None
                self.tail = node.prev
            node.next = None
            node.prev = None
            return node
        next_node = node.next
        prev_node = node.prev
        next_node.prev = prev_node
        prev_node.next = next_node
        node.next = None
        node.prev = None
        return node

    def pop_left(self) -> LinkedNode:
        return self.remove(self.head)

    def pop_right(self) -> LinkedNode:
        return self.remove(self.tail)

    def append_left(self, node: LinkedNode):
        self.length += 1
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node

    def append_right(self, node: LinkedNode):
        self.length += 1
        node.prev = self.tail
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node

    def print_from_head(self):
        cur = self.head
        while cur is not None:
            print(f"{cur.val} > ", end="")
            cur = cur.next
        print()

    def print_from_tail(self):
        cur = self.tail
        while cur is not None:
            print(f"{cur.val} > ", end="")
            cur = cur.prev
        print()

    def build_from_list(self, data: list[int]):
        for num in data:
            node = LinkedNode()
            node.val = num
            self.append_right(node)

    def exchange_next(self, cur: LinkedNode):
        if cur == self.tail: # last element can't be moved
            return
        prev_node = cur.prev
        next_node = cur.next

        if cur == self.head:
            self.head = next_node
        if next_node == self.tail: # become the tail after moving
            self.tail = cur

        cur.next = next_node.next
        cur.prev = next_node
        if prev_node is not None:
            prev_node.next = next_node
        if next_node.next is not None:
            next_node.next.prev = cur
        next_node.prev = prev_node
        next_node.next = cur