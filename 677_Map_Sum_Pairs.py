from collections import deque

class WeoTrieNode:
    def __init__(self, val:object=None):
        self.val = val
        self.ch = ""
        self.parent: WeoTrieNode = None
        self.children = dict[str, WeoTrieNode]()
        self.val = 0

class WeoTrie:
    def __init__(self):
        self.root = WeoTrieNode()

    def add_word(self, word: str, val: int):
        cur = self.root
        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                new_node = WeoTrieNode()
                new_node.parent = cur
                cur.children[ch] = new_node
                new_node.ch = ch
                cur = new_node
        cur.val += val

    def get_word(self, word: str) -> int:
        cur = self.root
        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                return 0
        return cur.val

    def print(self):
        q = deque()
        q.append(self.root)
        while len(q) > 0:
            node_list = []
            # print(len(q))
            while len(q) > 0:
                cur = q.popleft()
                for key, child in cur.children.items():
                    print(key, end=" ")
                    node_list.append(child)
            print()
            for n in node_list:
                q.append(n)


class MapSum:

    def __init__(self):
        self.trie = WeoTrie()

    def insert(self, key: str, val: int) -> None:
        self.trie.add_word(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.get_word(prefix)
