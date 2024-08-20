from typing import List

def is_similar(word1: str, word2: str) -> bool:
    quota_used = False
    diff_ch = ""
    for i, ch in enumerate(word1):
        if ch != word2[i]:
            if quota_used:
                return False
            elif diff_ch == "":
                diff_ch = ch
            elif diff_ch == word2[i]:
                quota_used = True
            elif diff_ch != word2[i]:
                return False
    return True

# print(is_similar("rats", "star"))

class WeightedUnionFind:

    def __init__(self, size):
        self.node = [i for i in range(size)]
        self.size = [1] * size
        self.count = size
        pass

    def find(self, p: int):
        while self.node[p] != p:
            p = self.node[p]
        return p

    def union(self, p: int, q: int):
        p = self.find(p)
        q = self.find(q)
        if p == q:
            return
        if self.size[p] < self.size[q]:
            self.node[p] = q
            self.size[q] = self.size[q] + self.size[p]
        else:
            self.node[q] = p
            self.size[p] = self.size[q] + self.size[p]
        self.count -= 1

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        wuf = WeightedUnionFind(len(strs))
        for i, s1 in enumerate(strs):
            for j in range(i + 1, len(strs)):
                s2 = strs[j]
                if is_similar(s1, s2):
                    print(s1, s2)
                    wuf.union(i, j)
        return wuf.count


r = Solution().numSimilarGroups(["tars","rats","arts","star"])
print(r)