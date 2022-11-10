from collections import deque

class WeoTrieNode:
    def __init__(self, val:object=None):
        self.val = val
        self.ch = ""
        self.parent: WeoTrieNode = None
        self.children = dict[str, WeoTrieNode]()
        self.word_end = False

    def __str__(self):
        return f"{self.ch}: children={self.children}"

class WeoTrie:
    def __init__(self):
        self.root = WeoTrieNode()

    def add_word(self, word: str):
        cur = self.root
        for i, ch in enumerate(word):
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                new_node = WeoTrieNode()
                new_node.parent = cur
                cur.children[ch] = new_node
                new_node.ch = ch
                cur = new_node
            if i == len(word) - 1:
                cur.word_end = True

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

class WordDictionary:

    def __init__(self):
        self.trie = WeoTrie()

    def addWord(self, word: str) -> None:
        self.trie.add_word(word)
        # self.trie.print()

    def search(self, word: str) -> bool:
        stk = [self.trie.root]
        for i, ch in enumerate(word):
            new_stk = []
            if len(stk) == 0:
                return False
            while len(stk) > 0:
                node = stk.pop()
                if ch == ".":
                    new_stk.extend(node.children.values())
                elif ch in node.children:
                    new_stk.append(node.children[ch])
            stk = new_stk
            if i == len(word) - 1:
                for node in stk:
                    if node.word_end:
                        return True
        return False

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("abd")
param_2 = obj.search("a.d")
print(param_2)