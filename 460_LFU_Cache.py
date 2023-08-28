from collections import defaultdict


class LinkedNode:
    def __init__(self):
        self.prev: LinkedNode = None
        self.next: LinkedNode = None
        self.counter: int = 0
        self.key_set = set[int]()

class DoubleLinkedList:
    def __init__(self):
        self.head: LinkedNode = None
        self.tail: LinkedNode = None
        self.key_node_dict = dict[int, LinkedNode]()
        self.length = 0


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
            print(f"({cur.key_set}, {cur.counter}) > ", end="")
            cur = cur.next
        print()

    def print_from_tail(self):
        cur = self.tail
        while cur is not None:
            print(f"({cur.key_set}, {cur.counter}) > ", end="")
            cur = cur.prev
        print()

    # node should be in the list
    def remove(self, node: LinkedNode) -> LinkedNode:
        self.length -= 1
        if node.prev is None:  # head
            if node.next is None:
                self.head = None
                self.tail = None
            else:
                node.next.prev = None
                self.head = node.next
            node.next = None
            node.prev = None
            return node
        if node.next is None:  # tail
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


    def update(self, key: int):
        node: LinkedNode = self.key_node[key]
        # delete current key
        if len(node.key_set) == 1:
            self.remove(node)
        else:
            node.key_set.remove(key)
        # update counter

        if node.next is not None and node.next.counter == node.counter + 1:
            # just delete current and merge to the next one
            node.next.key_set.add(key)
        else:
            # insert a new node between next one
            new_node = LinkedNode()
            new_node.counter = node.counter + 1
            new_node.key_set.add(key)

            new_node.prev = node.prev
            new_node.next = node.next
            if node.next is not None:
                node.next.prev = new_node
            else:
                self.tail = new_node
            if node.prev is not None:
                node.prev.next = new_node
            else:
                self.head = new_node


    def build_from_list(self, data: list[int]):
        for i, num in enumerate(data):
            node = LinkedNode()
            node.counter = num
            node.key_set.add(i)
            self.append_right(node)


dll = DoubleLinkedList()
dll.build_from_list([1, 2, 2])
dll.update(2)
dll.print_from_head()

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = dict[int, int]()
        self.counter_key = defaultdict(lambda : set[int]())
        self.key_counter = dict[int, int]()
        self.key_tick = dict[int, int]()
        self.tick = 0
        self.min_counter = 1

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.use_key(key)
        else:
            self.add_key(key)
        self.data[key] = value


    def use_key(self, key: int):
        self.tick += 1
        self.key_tick[key] = self.tick
        cnt = self.key_counter[key]
        self.counter_key[cnt].remove(key)
        self.counter_key[cnt + 1].add(key)
        if len(self.counter_key[cnt]) == 0:
            self.min_counter += 1

    def add_key(self, key: int):
        self.tick += 1
        self.key_tick[key] = self.tick

    def remove(self):
        self.min_counter


class Tester:
    def __init__(self, method_list: list[str], para_list: list[list[int]]):
        self.method_list = method_list
        self.para_list = para_list

    def run_test(self):
        lfu_cache = None
        for i, method in enumerate(self.method_list):
            if method == "LFUCache":
                r = lfu_cache = LFUCache(*self.para_list[i])
            elif method == "put":
                r = lfu_cache.put(*self.para_list[i])
            elif method == "get":
                r = lfu_cache.get(*self.para_list[i])
            print(i, method, self.para_list[i], r)
            if lfu_cache is not None:
                lfu_cache.lfu_queue.print_from_head()

# tester = Tester(
#     ["LFUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
#     , [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
# )
tester = Tester(
    ["LFUCache", "put", "get"]
    , [[0], [0, 0], [0]]
)
tester.run_test()


# dll = DoubleLinkedList()
# dll.build_from_list([3, 2, 1, 4, 8])
# dll.exchange_next(dll.tail.prev.prev)
# dll.print_from_head()
# dll.print_from_tail()