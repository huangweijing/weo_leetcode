class Solution:

    def __init__(self):
        self.cache = dict[str, str]()

    def get_key(self, word1, word2):
        return word1 + "_" + word2

    def get_lcs(self, word1: str, word2: str):
        key = self.get_key(word1, word2)
        if key in self.cache:
            return self.cache[key]
        if len(word1) == 0 or len(word2) == 0:
            return ""
        if word1[-1] == word2[-1]:
            result_lcs =  self.get_lcs(word1[:-1], word2[:-1]) + word1[-1]
        else:
            lcs1 = self.get_lcs(word1, word2[:-1])
            lcs2 = self.get_lcs(word1[:-1], word2)
            result_lcs = lcs1 if len(lcs1) > len(lcs2) else lcs2
        self.cache[key] = result_lcs
        return result_lcs
    
    def minDistance(self, word1: str, word2: str) -> int:
        result_lcs = self.get_lcs(word1, word2)
        return len(word1) + len(word2) - len(result_lcs) * 2



sol = Solution()
# lcs = sol.get_lcs("abasdfasdfasdfsadfasdfc", "addasdfsadfsasdfsadfsadfasdfasdfasdfsadfsadfasdadfasdfcdd")
# print(lcs)
print(sol.minDistance("sea", "eat"))