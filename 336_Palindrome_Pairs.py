from typing import List
from collections import deque

class WeoTrieNode:
    def __init__(self):
        self.word_idx_list = []
        self.ch = ""
        self.parent: WeoTrieNode = None
        self.children = dict[str, WeoTrieNode]()

class WeoTrie:
    def __init__(self):
        self.root = WeoTrieNode()

    def add_word(self, node: WeoTrieNode, word: str, ch_idx: int, word_idx: int, back:bool=False):
        # print(word, ch_idx)
        if len(word) == ch_idx:
            print("added")
            node.word_idx_list.append(word_idx)
            return
        ch = word[ch_idx]
        if node.ch == ch:
            self.add_word(node.parent, word, ch_idx + 1, word_idx, True)
        if ch not in node.children and not back:
            new_node = WeoTrieNode()
            new_node.parent = node
            node.children[ch] = new_node
            new_node.ch = ch
            print(f"added {ch}")
        if ch in node.children:
            self.add_word(node.children[ch], word, ch_idx + 1, word_idx, back)


    def print(self):
        q = deque()
        q.append(self.root)
        while len(q) > 0:
            node_list = []
            # print(len(q))
            while len(q) > 0:
                cur = q.popleft()
                print(cur.ch, cur.word_idx_list, end=" ")
                for key, child in cur.children.items():
                    node_list.append(child)
            print()
            for n in node_list:
                q.append(n)


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pass

wt = WeoTrie()
word_list = ["abcb"]
wt.add_word(wt.root, word_list[0], 0, 0)
wt.print()
