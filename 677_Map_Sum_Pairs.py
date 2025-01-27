class WeoTrieNode:
    def __init__(self, val:object=0):
        self.val = val
        self.ch = ""
        self.parent: WeoTrieNode = None
        self.children = dict[str, WeoTrieNode]()

class WeoTrie:
    def __init__(self):
        self.root = WeoTrieNode()
        self.key_val = dict[str, int]()

    def add_word(self, word: str, val: int):
        new_val = val
        if word in self.key_val:
            new_val = val - self.key_val[word]
        self.key_val[word] = val
        val = new_val
        cur = self.root
        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
                cur.val += val
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


class MapSum:

    def __init__(self):
        self.trie = WeoTrie()

    def insert(self, key: str, val: int) -> None:
        self.trie.add_word(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.get_word(prefix)


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("apple",3)
obj.insert("app", 2)
obj.insert("apple", 5)
obj.insert("apple", 1)
print(obj.sum("apple"))