from collections import deque

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

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_queue = DoubleLinkedList()
        self.cache = dict[int, LinkedNode]()

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        self.use_key(key)
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        # self.key_queue.print_from_head()
        if key in self.cache.keys():
            self.use_key(key)
            self.cache[key].val = value
            return
        if self.key_queue.length + 1 > self.capacity:
            pop_node = self.key_queue.pop_left()
            del self.cache[pop_node.key]
        node = LinkedNode()
        node.val = value
        node.key = key
        self.key_queue.append_right(node)
        self.cache[key] = node

    def use_key(self, key: int):
        node = self.cache[key]
        self.key_queue.remove(node)
        self.key_queue.append_right(node)

class Tester:
    def __init__(self, method_list: list[str], para_list: list[list[int]]):
        self.method_list = method_list
        self.para_list = para_list

    def run_test(self):
        for i, method in enumerate(self.method_list):
            if method == "LRUCache":
                r =lru_cache = LRUCache(*self.para_list[i])
            elif method == "put":
                r = lru_cache.put(*self.para_list[i])
            elif method == "get":
                r = lru_cache.get(*self.para_list[i])
            print(i, method, self.para_list[i], r)

tester = Tester(
    ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
    , [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
)
tester.run_test()