from typing import List


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
    
    def max_prefix_len(self, word: str) -> int:
        cur = self.root
        max_len = 0
        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
                max_len += 1
            else:
                return max_len
        return max_len


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = WeoTrie()
        for num in arr1:
            trie.add_word(str(num))
        ans = 0
        for num in arr2:
            prelen = trie.max_prefix_len(str(num))
            ans = max(ans, prelen)
        return ans
    

data = [
    [1,26]
    , [22,2]
]
r = Solution().longestCommonPrefix(*data)
print(r)