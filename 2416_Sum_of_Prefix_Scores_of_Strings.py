from typing import List

class WeoTrieNode:
    def __init__(self, val:object=None):
        self.val = val
        self.ch = ""
        self.parent: WeoTrieNode = None
        self.children = dict[str, WeoTrieNode]()
        self.score = 1

class WeoTrie:
    def __init__(self):
        self.root = WeoTrieNode()

    def add_word(self, word: str):
        cur = self.root
        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
                cur.score += 1
            else:
                new_node = WeoTrieNode()
                new_node.parent = cur
                cur.children[ch] = new_node
                new_node.ch = ch
                cur = new_node
    
    def get_score(self, word: str):
        score = 0
        cur = self.root
        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
                score += cur.score
            else:
                break
        return score


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = WeoTrie()
        for word in words:
            trie.add_word(word)
        ans = []
        for word in words:
            score = trie.get_score(word)
            ans.append(score)
        return ans
    
data = [
    ["abc","ab","bc","b"]
]
r = Solution().sumPrefixScores(*data)
print(r)
        