from typing import List


class WeoTrieNode:
    def __init__(self, val:int=0):
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
            cur.val += 1

    def val(self, prefix: str) -> int:
        cur = self.root
        for ch in prefix:
            if ch in cur.children:
                cur = cur.children[ch]
            else:
                return 0
        return cur.val



class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        wt = WeoTrie()
        for word in words:
            wt.add_word(word)
        return wt.val(pref)

r = Solution().prefixCount(["aaa", "a"], "aa")
print(r)

