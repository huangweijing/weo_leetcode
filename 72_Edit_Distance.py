class Solution:
    def max_seq_len(self, word1: str, word2: str) -> int:
        if len(word1) == 0 or len(word2) == 0:
            return 0

        if word1[-1] == word2[-1]:
            return self.max_seq_len(word1[:-1], word2[:-1]) + 1
        else:
            msl1 = self.max_seq_len(word1[:-1], word2)
            msl2 = self.max_seq_len(word1, word2[:-1])
            if msl1 == msl2:
                return msl1
            else:
                return max(msl1, msl2)

    def minDistance(self, word1: str, word2: str) -> int:
        seq_len = self.max_seq_len(word1, word2)
        return len(word1) + len(word2) - seq_len * 2

sol = Solution()
msl = sol.max_seq_len("abddddc", "dddabddaddcccdddddddddddddddc")
print(msl)