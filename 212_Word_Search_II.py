from typing import List
from collections import defaultdict


class WeoTrieNode:
    def __init__(self, val:object=None):
        self.val = val
        self.ch = ""
        self.parent: WeoTrieNode = None
        self.children = dict[str, WeoTrieNode]()
        self.children_set = set[str]()
        self.word = ""
        self.found = False
        self.child_found = 0
    
    def set_found(self):
        if len(self.children) == 0:
            self.found = True
        elif self.child_found == len(self.children):
            self.found = True
        if self.parent is not None:
            self.child_found += 1
            self.parent.set_found()


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
                cur.children_set.add(ch)
                new_node.ch = ch
                cur = new_node
        cur.word = word


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        w, h = len(board[0]), len(board)
        trie = WeoTrie()
        for word in words:
            trie.add_word(word)
        ans = list[str]()
        direct = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        def get_adjecent(cur_node: int, val: str, visited: set[int]) -> set[int]:
            row_idx, col_idx = cur_node // w, cur_node % w
            ret = set[int]()
            for d in direct:
                if 0 <= row_idx + d[0] < h and 0 <= col_idx + d[1] < w:
                    if val == board[row_idx + d[0]][col_idx + d[1]]:
                        if (row_idx + d[0]) * w + col_idx + d[1] not in visited:
                            ret.add((row_idx + d[0]) * w + col_idx + d[1])
            return ret

        # cur_nodes: nodes satisfied root children, visited nodes before func
        def trav_trie(root: WeoTrieNode, cur_node: int, visited: set[int]):
            if root.found:
                return
            if len(root.word) > 0:
                print(root.word, root.found)
                ans.append(root.word)
                root.set_found()
                # return
            visited.add(cur_node)
            for child_node in root.children.values():
                adj_list = get_adjecent(cur_node, child_node.ch, visited)
                # print("adj>>", cur_node, child_node.ch, visited, adj_list, ans)
                for adj in adj_list:
                    trav_trie(child_node, adj, visited)
            visited.remove(cur_node)

        start_dict = defaultdict(lambda: set[int]())
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                start_dict[val].add(i * w + j)
        for ch, child in trie.root.children.items():
            for cur in start_dict[ch]:
                # print(ch, cur)
                trav_trie(child, cur, set[int]())
        return list(ans)


data = [
    [["a","b","c","e"],
     ["x","x","c","d"],
     ["x","x","b","a"]]
    , ["abc","abcd"]
]
# r = Solution().findWords(*data)
# print(r)

from functools import cache
@cache
def test(a: tuple) -> int:
    print(a)
    return sum(a)

# print(type({ }))
