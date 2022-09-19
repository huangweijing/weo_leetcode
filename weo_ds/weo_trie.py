from collections import deque

class WeoTrieNode:
    def __init__(self, val:object=None):
        self.val = val
        self.ch = ""
        self.parent: WeoTrieNode = None
        self.children = dict[str, WeoTrieNode]()

class WeoTrie:
    def __init__(self):
        self.root = WeoTrieNode()

    def add_word(self, word: str):
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


wt = WeoTrie()
wt.add_word("hello")
wt.add_word("helllo")
wt.add_word("aablo")
wt.print()
