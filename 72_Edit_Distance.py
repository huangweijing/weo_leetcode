from functools import cache


class Solution:
    def __init__(self):
        self.word1 = ""
        self.word2 = ""

    @cache
    def my_sol(self, word1_len: int, word2_len: int) -> int:
        if word1_len == 0 or word2_len == 0:
            return max(word1_len, word2_len)
        if self.word1[word1_len - 1] == self.word2[word2_len - 1]:
            return self.my_sol(word1_len - 1, word2_len - 1)
        else:
            # change a char
            sub1 = self.my_sol(word1_len - 1, word2_len - 1) + 1
            # add a char
            sub2 = self.my_sol(word1_len, word2_len - 1) + 1
            # delete a char
            sub3 = self.my_sol(word1_len - 1, word2_len) + 1
            return min(sub1, sub2, sub3)

    def minDistance(self, word1: str, word2: str) -> int:
        self.word1, self.word2 = word1, word2
        return self.my_sol(len(word1), len(word2))

sol = Solution()
msl = sol.minDistance("horse", "ros")
print(msl)

# result = [x for x in [1, 4, 8, 0, 3, 12, 32] if x > 5]
# print(result)

a1 = [1, 4, 8]
a2 = [9, 7, 3]
l1 = (list(zip(a1, a2)))
l1.sort(key=lambda x: x[1], reverse=True)
print(l1)