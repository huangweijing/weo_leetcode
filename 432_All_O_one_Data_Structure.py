class Node:
    def __init__(self, cnt: int, prv=None, nxt=None):
        self.cnt = cnt
        self.next_node: Node = nxt
        self.prev_node: Node = prv
        self.str_set = set[str]()

    def inc(self, key: str):
        self.str_set.remove(key)
        insert_node = None
        if self.next_node:
            if self.next_node.cnt == self.cnt + 1:
                self.next_node.str_set.add(key)
            else:
                new_node = Node(self.cnt + 1)
                new_node.next_node = self.next_node
                new_node.prev_node = self
                new_node.str_set.add(key)
                self.next_node.prev_node = new_node
                self.next_node = new_node
            insert_node = self.next_node
        else:
            new_node = Node(self.cnt + 1)
            new_node.next_node = self.next_node
            new_node.prev_node = self
            new_node.str_set.add(key)
            self.next_node = new_node
            insert_node = new_node
        if len(self.str_set) == 0 and self.cnt != 1:
            if self.next_node:
                self.next_node.prev_node = self.prev_node
                self.prev_node.next_node = self.next_node
            else:
                self.prev_node.next_node = None
        return insert_node

    def dec(self, key: str):
        val_node = None
        self.str_set.remove(key)
        if self.cnt == 1:
            return None
        elif self.prev_node:
            if self.prev_node.cnt == self.cnt - 1:
                self.prev_node.str_set.add(key)
                val_node = self.prev_node
            else:
                new_node = Node(self.cnt - 1)
                new_node.prev_node = self.prev_node
                new_node.next_node = self
                new_node.str_set.add(key)
                # if self.prev_node:
                self.prev_node.next_node = new_node
                self.prev_node = new_node
                val_node = new_node
            if len(self.str_set) == 0:
                if self.next_node:
                    self.next_node.prev_node = self.prev_node
                    self.prev_node.next_node = self.next_node
                else:
                    self.prev_node.next_node = None
        return val_node


class AllOne:

    def __init__(self):
        self.head = Node(cnt=1)
        self.last = self.head
        self.str_node = dict[str, Node]()
        self.max_cnt = 0

    def inc(self, key: str) -> None:
        if key in self.str_node:
            node = self.str_node[key]
            res = node.inc(key)
            self.str_node[key] = res
            if res.cnt > self.max_cnt:
                self.max_cnt = res.cnt
                self.last = res
        else:
            self.head.str_set.add(key)
            self.str_node[key] = self.head
            self.max_cnt = max(self.max_cnt, self.head.cnt)

    def dec(self, key: str) -> None:
        node = self.str_node[key]
        cnt = node.cnt
        res = node.dec(key)
        if res:
            self.str_node[key] = res
            if cnt == self.max_cnt and res.next_node is None:
                self.max_cnt = res.cnt
                self.last = res
        else:
            del self.str_node[key]
        if self.max_cnt == 1 and len(self.head.str_set) == 0:
            self.max_cnt = 0

    def getMaxKey(self) -> str:
        if self.max_cnt > 0:
            return next(iter(self.last.str_set))
        else:
            return ""

    def getMinKey(self) -> str:
        if self.max_cnt == 0:
            return ""
        else:
            if len(self.head.str_set) == 0:
                str_set = self.head.next_node.str_set
                return next(iter(str_set))
            else:
                return next(iter(self.head.str_set))

    def print(self):
        cur = self.head
        print(f"-----max_cnt={self.max_cnt}, min_key={self.getMinKey()}, max_key={self.getMaxKey()}-----")
        print("keys=", [[k, v.cnt] for k, v in self.str_node.items()])
        while cur is not None:
            print(f"cur.str_set={cur.str_set}", f"self.cnt={cur.cnt}", "->")
            cur = cur.next_node
        cur = self.last
        print("------")
        while cur is not None:
            print(f"cur.str_set={cur.str_set}", f"self.cnt={cur.cnt}", "->")
            cur = cur.prev_node
        print()


data = [
    # ["AllOne","inc","inc","getMaxKey","getMinKey","inc","inc","getMaxKey","getMinKey","dec","dec","dec"]
    # , [[],["hello"],["hello"],[],[],["leet"],["leet"],[],[],["hello"],["leet"],["hello"]]
    # ["AllOne","inc","inc","inc","inc","inc","inc","dec", "dec","getMinKey","dec","getMaxKey","getMinKey"]
    # , [[],["a"],["b"],["b"],["c"],["c"],["c"],["b"],["b"],[],["a"],[],[]]
    ["AllOne","inc","inc","inc","inc","inc","inc","getMaxKey","inc","dec","getMaxKey","dec","inc","getMaxKey","inc","inc","dec","dec","dec","dec","getMaxKey","inc","inc","inc","inc","inc","inc","getMaxKey","getMinKey"]
    , [[],["hello"],["world"],["leet"],["code"],["ds"],["leet"],[],["ds"],["leet"],[],["ds"],["hello"],[],["hello"],["hello"],["world"],["leet"],["code"],["ds"],[],["new"],["new"],["new"],["new"],["new"],["new"],[],[]]
]
ssa = AllOne()
result = []
for idx, command in enumerate(zip(data[0], data[1])):
    if idx == 0:
        continue
    print(command[0], command[1])
    ret = getattr(ssa, command[0])(* command[1])
    print(command[0], command[1], ret)
    result.append(ret)
    ssa.print()
print(result)
